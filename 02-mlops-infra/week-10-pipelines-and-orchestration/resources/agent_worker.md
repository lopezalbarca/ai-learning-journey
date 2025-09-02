# Prefect Local Server + Worker (Quick Start)

> Target timezone: **Europe/Madrid**. Cron in the deployment is already set to 09:00 Europe/Madrid.

## 0) Install deps and freeze
```bash
python -m venv .venv
source .venv/bin/activate   # (Windows: .\.venv\Scripts\Activate.ps1)
python -m pip install --upgrade pip
pip install -r env/requirements.base.txt
pip freeze > env/requirements.txt
```

## 1) Start the local Prefect server (new terminal)
```bash
prefect version
prefect server start
```
This boots the API + UI. Keep it running. The UI normally listens on http://127.0.0.1:4200/

## 2) Build & apply a scheduled deployment (another terminal)
```bash
source .venv/bin/activate
python exercises/04_build_deployment.py
```
You should see **daily-0900** created for `daily_job` (cron `0 9 * * *`, tz `Europe/Madrid`).

## 3) Start a worker to pick up scheduled runs
```bash
# Process-based worker with a custom queue for this week
prefect worker start -p process -q week-10
```
Leave it running. When the schedule triggers, the worker executes the flow and you’ll see logs in the terminal and in the UI.

## 4) Ad‑hoc run (optional)
```bash
python exercises/04_scheduling.py
```

## Notes
- You can tag deployments (we added `["week-10"]`) and route them via queues.
- For observability, the UI shows run durations, states, logs, and parameters.
- If you use Cloud later, switch the profile and skip `prefect server start`.
