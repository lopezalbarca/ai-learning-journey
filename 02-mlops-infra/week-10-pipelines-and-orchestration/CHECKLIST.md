# W10 · Checklist

### Setup (Python)
- [ ] Virtual environment created and activated.
- [ ] Dependencies installed (`prefect`, `pandas`, `scikit-learn`, `httpx`, `pydantic`).
- [ ] `env/requirements.txt` generated and committed.

### Flows & Dependencies
- [ ] `01_basic_flow.py` runs (`extract -> transform -> load`) and returns a result.
- [ ] Flow/Task boundaries are clear and logged.

### Retries, Timeouts & Backoff
- [ ] `02_retries_and_timeouts.py` demonstrates retries on transient errors.
- [ ] Task timeouts prevent indefinite hangs.
- [ ] (Nice-to-have) Exponential backoff + jitter implemented.

### Resilience Patterns
- [ ] `03_resilience_patterns.py` implements a **fallback** path.
- [ ] A simple **circuit breaker** prevents hammering a failing upstream.
- [ ] Runs record failure/success states with timestamps.

### Scheduling
- [ ] `04_scheduling.py` flow created.
- [ ] A **deployment** scheduled via cron (09:00 Europe/Madrid) is applied.
- [ ] Local agent/worker running and executing the schedule.

### .NET Orchestrator
- [ ] `src/Pipelines.Api` builds (`dotnet build`) and runs (`docker compose up`).
- [ ] `ETL_DEPLOYMENT_ID` set in `.env` and matches the Prefect deployment.
- [ ] `GET /healthz` returns OK.
- [ ] `POST /api/etl/start` returns a `run_id` and Prefect worker picks it up.
- [ ] `GET /api/etl/status/{run_id}` returns a valid state (e.g., Completed/Running).
- [ ] `GET /api/etl/runs` lists recent entries from `runs/metrics.csv`.

### Observability
- [ ] Run IDs, states, and durations captured (UI/CLI or CSV).
- [ ] Parameters/environment captured for reproducibility.

### Consolidation
- [ ] `04_conceptual_questions.md` answered.
- [ ] **Self‑eval:** I can explain the **end‑to‑end flow**: Pipelines.Api → Prefect API → Worker → Python flow → UI/CSV → Pipelines.Api.
