using System.Diagnostics.Metrics;
using System.Net.Http.Headers;
using Microsoft.AspNetCore.Http.HttpResults;
using Polly;
using Polly.Extensions.Http;

var builder = WebApplication.CreateBuilder(args);

var pyBaseUrl = Environment.GetEnvironmentVariable("PY_RAG_BASE_URL") ?? "http://localhost:8000";

var meter = new Meter("DocsQna.Api", "1.0.0");
var qaCounter = meter.CreateCounter<long>("qa_requests_total");
var qaLatency = meter.CreateHistogram<double>("qa_latency_ms");

builder.Services.AddHttpClient("py", client =>
{
    client.BaseAddress = new Uri(pyBaseUrl);
    client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
})
.AddPolicyHandler(HttpPolicyExtensions
    .HandleTransientHttpError()
    .OrResult(msg => (int)msg.StatusCode == 429)
    .WaitAndRetryAsync(new[]
    {
        TimeSpan.FromMilliseconds(200),
        TimeSpan.FromMilliseconds(500),
        TimeSpan.FromSeconds(1)
    }))
.AddPolicyHandler(Policy.TimeoutAsync<HttpResponseMessage>(TimeSpan.FromSeconds(30)))
.AddPolicyHandler(HttpPolicyExtensions
    .HandleTransientHttpError()
    .CircuitBreakerAsync(5, TimeSpan.FromSeconds(30)));

var app = builder.Build();

app.MapGet("/", () => Results.Json(new { ok = true, service = "DocsQna.Api", py = pyBaseUrl }));

app.MapPost("/api/ingest", async Task<Results<Ok<object>, BadRequest<string>>> (HttpRequest http, IHttpClientFactory factory) =>
{
    var payload = await http.ReadFromJsonAsync<object>();
    if (payload is null) return TypedResults.BadRequest("Invalid payload");

    var client = factory.CreateClient("py");
    var resp = await client.PostAsJsonAsync("/ingest", payload);
    if (!resp.IsSuccessStatusCode)
    {
        return TypedResults.BadRequest($"py-rag error: {(int)resp.StatusCode}");
    }
    var data = await resp.Content.ReadFromJsonAsync<object>();
    return TypedResults.Ok(data!);
});

app.MapPost("/api/qa", async Task<Results<Ok<object>, BadRequest<string>>> (HttpRequest http, IHttpClientFactory factory) =>
{
    qaCounter.Add(1);
    var started = DateTime.UtcNow;

    var payload = await http.ReadFromJsonAsync<object>();
    if (payload is null) return TypedResults.BadRequest("Invalid payload");

    var client = factory.CreateClient("py");
    var resp = await client.PostAsJsonAsync("/qa", payload);
    if (!resp.IsSuccessStatusCode)
    {
        return TypedResults.BadRequest($"py-rag error: {(int)resp.StatusCode}");
    }
    var data = await resp.Content.ReadFromJsonAsync<object>();

    var elapsed = (DateTime.UtcNow - started).TotalMilliseconds;
    qaLatency.Record(elapsed);

    return TypedResults.Ok(data!);
});

app.Run();
