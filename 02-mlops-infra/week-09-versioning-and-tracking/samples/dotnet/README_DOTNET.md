# .NET Serving Hook (Week 09)

This sample shows a **.NET 9 minimal API** that **proxies MLflow** so your enterprise stack can expose *read-only* experiment data behind your usual gateways/auth.

## Endpoints
- `GET /healthz` — liveness
- `GET /mlflow/experiments` — MLflow `experiments/list`
- `GET /mlflow/runs/{experimentId}` — MLflow `runs/search`
- `GET /mlflow/runs/{runId}/artifacts` — MLflow `artifacts/list`

> The API uses `HttpClientFactory` + Polly retries and a 10s timeout.

## Configuration
Set MLflow base URL in `appsettings.json` or env:
```bash
MLflow__BaseUrl=http://mlflow.local:5000
```

## Build & Run
```bash
dotnet build
dotnet run
# or with Docker
docker build -t tracking-api:latest .
docker run -p 8080:8080 -e MLflow__BaseUrl=http://host.docker.internal:5000 tracking-api:latest
```

## CI/CD (example)
See `.github/workflows/ci-dotnet-tracking-api.yml` for a GitHub Actions pipeline:
- Build & test
- Publish Docker image
- (Optional) Deploy to **Azure Container Apps** (or your platform)
