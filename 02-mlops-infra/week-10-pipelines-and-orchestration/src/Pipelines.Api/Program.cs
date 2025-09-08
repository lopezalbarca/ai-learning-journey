using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text;
using System.Text.Json;
using Polly;
using Polly.Extensions.Http;
using Serilog;

var builder = WebApplication.CreateBuilder(args);

// Serilog
builder.Host.UseSerilog((ctx, lc) => lc
    .MinimumLevel.Information()
    .WriteTo.Console());

// Config
var prefectApiBase = Environment.GetEnvironmentVariable("PREFECT_API_URL") ?? "http://localhost:4200/api/";
var etlDeploymentId = Environment.GetEnvironmentVariable("ETL_DEPLOYMENT_ID"); // required for /api/etl/start
var csvPath = Environment.GetEnvironmentVariable("CSV_PATH") ?? Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "runs", "metrics.csv");

builder.Services.AddHttpClient("prefect", client =>
{
    client.BaseAddress = new Uri(prefectApiBase);
    client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
})
.AddPolicyHandler(HttpPolicyExtensions.HandleTransientHttpError()
    .OrResult(msg => (int)msg.StatusCode == 429)
    .WaitAndRetryAsync(new[] {
        TimeSpan.FromMilliseconds(200),
        TimeSpan.FromMilliseconds(500),
        TimeSpan.FromSeconds(1),
        TimeSpan.FromSeconds(2)
    }))
.AddPolicyHandler(Policy.TimeoutAsync<HttpResponseMessage>(TimeSpan.FromSeconds(30)))
.AddPolicyHandler(HttpPolicyExtensions.HandleTransientHttpError()
    .CircuitBreakerAsync(5, TimeSpan.FromSeconds(30)));

var app = builder.Build();

app.MapGet("/healthz", () =>
{
    return Results.Json(new {
        ok = true,
        service = "Pipelines.Api",
        prefectApiBase,
        csvPath,
        etlDeploymentConfigured = !string.IsNullOrWhiteSpace(etlDeploymentId)
    });
});

app.MapPost("/api/etl/start", async (IHttpClientFactory httpFactory, ILogger<Program> log) =>
{
    if (string.IsNullOrWhiteSpace(etlDeploymentId))
    {
        return Results.Problem("ETL_DEPLOYMENT_ID is not configured. Set it in environment (compose) to the Prefect deployment ID.", statusCode: 500);
    }

    try
    {
        var client = httpFactory.CreateClient("prefect");
        var body = new {
            name = "api-triggered",
            state = new { type = "SCHEDULED" } // immediate scheduling
        };

        var resp = await client.PostAsJsonAsync($"deployments/{etlDeploymentId}/create_flow_run", body);
        if (!resp.IsSuccessStatusCode)
        {
            var text = await resp.Content.ReadAsStringAsync();
            log.LogWarning("Prefect create_flow_run failed: {Status} {Body}", (int)resp.StatusCode, text);
            return Results.Problem($"Prefect API error: {(int)resp.StatusCode}", statusCode: 502);
        }

        using var doc = JsonDocument.Parse(await resp.Content.ReadAsStringAsync());
        var runId = doc.RootElement.TryGetProperty("id", out var idProp) ? idProp.GetString() : null;
        runId ??= doc.RootElement.TryGetProperty("flow_run", out var fr) && fr.TryGetProperty("id", out var frId) ? frId.GetString() : null;
        if (string.IsNullOrWhiteSpace(runId))
        {
            log.LogWarning("Unable to parse flow run id from Prefect response");
            return Results.Problem("Unable to parse flow run id from Prefect response", statusCode: 502);
        }

        try
        {
            AppendCsv(new RunRecord(
                Timestamp: DateTime.UtcNow.ToString("yyyy-MM-ddTHH:mm:ssZ"),
                Flow: "etl",
                State: "scheduled",
                DurationMs: 0,
                Notes: runId!
            ), csvPath);
        }
        catch (Exception ex)
        {
            log.LogWarning(ex, "Failed to append run to CSV at {Path}", csvPath);
        }

        log.LogInformation("Triggered Prefect ETL run {RunId}", runId);
        return Results.Ok(new { run_id = runId, status = "scheduled" });
    }
    catch (Exception ex)
    {
        log.LogError(ex, "Error triggering ETL run");
        return Results.Problem("Internal error triggering flow", statusCode: 500);
    }
});

app.MapGet("/api/etl/runs", (ILogger<Program> log) =>
{
    try
    {
        if (!File.Exists(csvPath))
        {
            return Results.Json(Array.Empty<RunRecord>());
        }
        var rows = ReadCsv(csvPath);
        var ordered = rows.Reverse().Take(50).ToArray();
        return Results.Json(ordered);
    }
    catch (Exception ex)
    {
        log.LogError(ex, "Error reading CSV at {Path}", csvPath);
        return Results.Problem("Failed to read runs CSV", statusCode: 500);
    }
});

app.MapGet("/api/etl/status/{runId}", async (string runId, IHttpClientFactory factory, ILogger<Program> log) =>
{
    try
    {
        var client = factory.CreateClient("prefect");
        var resp = await client.GetAsync($"flow_runs/{runId}");
        if (resp.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            return Results.NotFound(new { run_id = runId, state = "unknown" });
        }
        if (!resp.IsSuccessStatusCode)
        {
            var text = await resp.Content.ReadAsStringAsync();
            log.LogWarning("Prefect flow_runs failed: {Status} {Body}", (int)resp.StatusCode, text);
            return Results.Problem("Prefect API error", statusCode: 502);
        }

        using var doc = JsonDocument.Parse(await resp.Content.ReadAsStringAsync());
        string? stateName = null;
        if (doc.RootElement.TryGetProperty("state", out var stateElem))
        {
            if (stateElem.TryGetProperty("name", out var nameProp))
                stateName = nameProp.GetString();
            else if (stateElem.TryGetProperty("type", out var typeProp))
                stateName = typeProp.GetString();
        }
        stateName ??= "unknown";
        return Results.Ok(new { run_id = runId, state = stateName });
    }
    catch (Exception ex)
    {
        log.LogError(ex, "Error getting run status");
        return Results.Problem("Internal error", statusCode: 500);
    }
});

app.Run();

// CSV helpers and record
static IEnumerable<RunRecord> ReadCsv(string path)
{
    using var fs = File.OpenRead(path);
    using var sr = new StreamReader(fs, Encoding.UTF8, detectEncodingFromByteOrderMarks: true);
    var lineNo = 0;
    string? line;
    while ((line = sr.ReadLine()) is not null)
    {
        lineNo++;
        if (lineNo == 1 && line.StartsWith("timestamp")) continue; // header
        var parts = SplitCsv(line);
        if (parts.Length < 5) continue;
        yield return new RunRecord(
            Timestamp: parts[0],
            Flow: parts[1],
            State: parts[2],
            DurationMs: int.TryParse(parts[3], out var d) ? d : 0,
            Notes: parts[4]
        );
    }
}

static void AppendCsv(RunRecord row, string path)
{
    var dir = Path.GetDirectoryName(path);
    if (!string.IsNullOrWhiteSpace(dir)) Directory.CreateDirectory(dir);
    var fileExists = File.Exists(path);
    using var fs = new FileStream(path, FileMode.Append, FileAccess.Write, FileShare.Read);
    using var sw = new StreamWriter(fs, new UTF8Encoding(false));
    if (!fileExists)
    {
        sw.WriteLine("timestamp,flow,state,duration_ms,notes");
    }
    sw.WriteLine($"{row.Timestamp},{row.Flow},{row.State},{row.DurationMs},{EscapeCsv(row.Notes)}");
}

static string[] SplitCsv(string line)
{
    var result = new List<string>();
    var sb = new StringBuilder();
    bool inQuotes = false;
    for (int i = 0; i < line.Length; i++)
    {
        var c = line[i];
        if (c == '"')
        {
            if (inQuotes && i + 1 < line.Length && line[i + 1] == '"')
            {
                sb.Append('"');
                i++;
            }
            else
            {
                inQuotes = !inQuotes;
            }
        }
        else if (c == ',' && !inQuotes)
        {
            result.Add(sb.ToString());
            sb.Clear();
        }
        else
        {
            sb.Append(c);
        }
    }
    result.Add(sb.ToString());
    return result.ToArray();
}

static string EscapeCsv(string? s)
{
    s ??= string.Empty;
    if (s.Contains(',') || s.Contains('"') || s.Contains('\'))
    {
        return $""{s.Replace(""", """")}"";
    }
    return s;
}

public readonly record struct RunRecord(
    string Timestamp,
    string Flow,
    string State,
    int DurationMs,
    string Notes
);
