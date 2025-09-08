using System.Net.Http.Json;
using Polly;
using Polly.Extensions.Http;

var builder = WebApplication.CreateBuilder(args);

// Config
var mlflowBase = builder.Configuration.GetValue<string>("MLflow:BaseUrl") ?? "http://localhost:5000";

builder.Services.AddHttpClient("mlflow", c =>
{
    c.BaseAddress = new Uri(mlflowBase.TrimEnd('/') + "/api/2.0/mlflow/");
    c.Timeout = TimeSpan.FromSeconds(10);
})
.AddPolicyHandler(HttpPolicyExtensions
    .HandleTransientHttpError()
    .WaitAndRetryAsync(new[] { TimeSpan.FromMilliseconds(200), TimeSpan.FromMilliseconds(500), TimeSpan.FromMilliseconds(1000) }));

var app = builder.Build();

app.MapGet("/healthz", () => Results.Ok(new { status = "ok" }));

// GET /mlflow/experiments -> proxy to MLflow list experiments
app.MapGet("/mlflow/experiments", async (IHttpClientFactory factory, CancellationToken ct) =>
{
    var client = factory.CreateClient("mlflow");
    var resp = await client.GetAsync("experiments/list", ct);
    resp.EnsureSuccessStatusCode();
    return Results.Stream(await resp.Content.ReadAsStreamAsync(ct), contentType: "application/json");
});

// GET /mlflow/runs/{experimentId}
app.MapGet("/mlflow/runs/{experimentId}", async (string experimentId, IHttpClientFactory factory, CancellationToken ct) =>
{
    var client = factory.CreateClient("mlflow");
    var payload = new { experiment_ids = new[] { experimentId } };
    var resp = await client.PostAsJsonAsync("runs/search", payload, ct);
    resp.EnsureSuccessStatusCode();
    return Results.Stream(await resp.Content.ReadAsStreamAsync(ct), contentType: "application/json");
});

// GET /mlflow/runs/{runId}/artifacts -> list artifacts for a run
app.MapGet("/mlflow/runs/{runId}/artifacts", async (string runId, IHttpClientFactory factory, CancellationToken ct) =>
{
    var client = factory.CreateClient("mlflow");
    var url = $"artifacts/list?run_id={Uri.EscapeDataString(runId)}";
    var resp = await client.GetAsync(url, ct);
    resp.EnsureSuccessStatusCode();
    return Results.Stream(await resp.Content.ReadAsStreamAsync(ct), contentType: "application/json");
});

app.Run();
