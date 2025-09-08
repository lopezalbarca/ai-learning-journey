# W10 · Pipelines & Orchestration (MLOps & Infra)

**Goal:** Design robust pipelines using **Prefect 2** (flows, tasks, scheduling, retries, timeouts, backoff, circuit breaker) **and** add a **.NET 8 Minimal API** that orchestrates these flows with production‑minded resilience (Polly). By the end, you’ll run your ETL on a schedule, trigger it via HTTP, and observe runs end‑to‑end.

---

## Learning outcomes
- Model workflows as **flows** and **tasks** with clear dependencies.
- Configure **retries**, **timeouts**, and **exponential backoff** for transient errors.
- Add **fallback/circuit‑breaker** style resilience at the flow level.
- Create a **scheduled deployment** (cron) with timezone **Europe/Madrid**.
- Orchestrate flows from a **.NET 8 Minimal API** with **HttpClientFactory + Polly** (retries, timeouts, circuit breaker).
- Log and persist **run metadata** (ids, states, durations) for observability.

> We use **Prefect 2** locally for a smooth dev experience. Concepts translate well to Airflow later if you prefer.

---

## Prerequisites
- **Python 3.11+**
- **.NET SDK 8.0+**
- **Docker & Docker Compose**
- Basic familiarity with Weeks 08–09 (project structure, logging/metrics mindset).

---

## Plan: Your Step-by-Step Guide

### 1) Prepare your Python lab
```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
# .\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt
```
Base deps: `prefect`, `pandas`, `scikit-learn`, `httpx`, `pydantic`.

---

### 2) First flow with dependencies
Open `exercises/01_basic_flow.py` and run it:
```bash
python exercises/01_basic_flow.py
```
**Observe** the dependency graph: `extract -> transform -> load`, and that the **flow** is the orchestration boundary.

---

### 3) Retries, timeouts & backoff
Open and run:
```bash
python exercises/02_retries_and_timeouts.py
```
- `retries=3` + `retry_delay_seconds=2` gives basic backoff (augment with jitter if you want).
- `timeout_seconds` prevents hung tasks from blocking forever.

> Tip: For exponential backoff with jitter, adapt a loop and `time.sleep(min(max_delay, base * 2**attempt + random.random()))` on exceptions.

---

### 4) Resilience patterns (fallback & circuit breaker)
Open and run:
```bash
python exercises/03_resilience_patterns.py
```
- **Circuit breaker** avoids hammering a failing upstream.
- **Fallback** ensures graceful degradation instead of full failure.

---

### 5) Scheduling the flow (cron, Europe/Madrid)
Create the scheduled deployment for `daily_job`:
```bash
# Build & apply deployment (cron 09:00 Europe/Madrid)
python exercises/04_build_deployment.py
```
This registers a deployment (e.g., `daily_job / daily-0900`) in Prefect. You can verify later in the UI.

---

### 6) Bring up the orchestration stack (Docker Compose)
We’ll run **Prefect Orion (UI/API)**, a **Prefect Worker**, and the **.NET Orchestrator (Pipelines.Api)**.

**6.1) Get the deployment ID**
```bash
docker compose run --rm prefect-worker bash -lc "prefect deployment ls"
# copy the ID for daily_job/daily-0900 (or your chosen deployment)
```

**6.2) Set environment and start the stack**
Create a `.env` file next to `docker-compose.yml`:
```env
ETL_DEPLOYMENT_ID=<paste-the-deployment-id-here>
```
Then build and launch:
```bash
docker compose build
docker compose up
```
- Prefect UI → http://localhost:4200  
- Pipelines.Api → http://localhost:8080/healthz

**What’s running:**
- `prefect-server`: Orion UI + API (`http://prefect-server:4200` inside the network).
- `prefect-worker`: listens on queue **week-10** and executes flows from `exercises/` (mounted).
- `pipelines-api`: .NET 8 Minimal API that triggers/checks flows via Prefect API.

---

### 7) Trigger & monitor via .NET
**Start a flow run**:
```bash
curl -X POST http://localhost:8080/api/etl/start
# → {"run_id":"<uuid>","status":"scheduled"}
```
**Check status**:
```bash
curl http://localhost:8080/api/etl/status/<uuid>
# → {"run_id":"<uuid>","state":"Completed"}
```
**List recent runs** (reads `runs/metrics.csv`):
```bash
curl http://localhost:8080/api/etl/runs
```
> CSV schema: `timestamp,flow,state,duration_ms,notes`. The .NET API appends a row on submission; the Python logger in `exercises/05_run_logger.py` appends outcome/duration if you run flows ad‑hoc from Python.

---

### 8) Observability checklist
- Log **run IDs**, **start/end times**, and **states** (UI/CLI + CSV).
- Capture **task durations** (Prefect UI already shows this).
- Keep **parameters & env** in run metadata (reproducibility).
- Use a **correlation ID** per run if you call external systems.

---

### 9) Troubleshooting (Common Issues)
- **UI Port Conflict (4200)** → run on a different port:
  ```bash
  prefect server start --host 127.0.0.1 --port 4300
  ```
- **Worker Queue Mismatch** → deployment tagged `"week-10"`; worker must start with `-q week-10`.
- **API URL Differences** → local: `http://127.0.0.1:4200/api`; in compose: `http://prefect-server:4200/api`.
- **Missing Packages (`ModuleNotFoundError`)** → venv not active or deps not installed. Reinstall from `env/requirements.txt`.
- **Deployment Not Running** → ensure **server** and a **worker** are running; without worker, schedules won’t execute.
- **Stale/Orphan Runs** → restart server + worker; consider removing `.prefect/` if local state corrupted.

---

## Deliverables
- `env/requirements.txt` frozen.
- Runnable examples in `exercises/`:
  - `01_basic_flow.py`
  - `02_retries_and_timeouts.py`
  - `03_resilience_patterns.py`
  - `04_scheduling.py` (+ `04_build_deployment.py`)
  - (optional) `05_run_logger.py` for CSV logging
- **Deployment** created (daily cron at 09:00 Europe/Madrid) and visible in UI.
- **Docker Compose** stack up (Prefect server + worker + Pipelines.Api).
- .NET endpoints tested: `/healthz`, `POST /api/etl/start`, `GET /api/etl/status/{id}`, `GET /api/etl/runs`.
- Short CSV/Markdown note capturing a few run IDs, states, and durations.

---

## Folder layout (Week 10)
```
02-mlops-infra/
  week-10-pipelines-and-orchestration/
    README.md
    CHECKLIST.md
    .gitignore
    docker-compose.yml
    env/
      setup.ps1
      setup.sh
      requirements.base.txt
      requirements.txt
    resources/
      links.md
      agent_worker.md
    exercises/
      01_basic_flow.py
      02_retries_and_timeouts.py
      03_resilience_patterns.py
      04_scheduling.py
      04_build_deployment.py
      05_run_logger.py
      04_conceptual_questions.md
    runs/
      metrics.csv
      .gitkeep
    src/
      Pipelines.Api/
        Pipelines.Api.csproj
        Program.cs
        Dockerfile
```
