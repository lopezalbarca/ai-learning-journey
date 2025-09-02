# Links

## Prefect 2 (primary for this week)
- Getting Started: https://docs.prefect.io/latest/getting-started/installation/
- Flows & Tasks: https://docs.prefect.io/latest/concepts/flows-and-tasks/
- Deployments & Schedules: https://docs.prefect.io/latest/deploy/infrastructure-and-schedules/
- Retries & Timeouts: https://docs.prefect.io/latest/concepts/tasks/#retries-and-retry-behavior
- Orion UI / Observability: https://docs.prefect.io/latest/ui/overview/

## Airflow (alternate orchestrator)
- Concepts (DAGs, Operators, Sensors): https://airflow.apache.org/docs/apache-airflow/stable/concepts/index.html
- Scheduling & Timetables: https://airflow.apache.org/docs/apache-airflow/stable/scheduling.html
- Retries, SLAs: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tu.html#retries

## Resilience Patterns
- Circuit Breaker (Martin Fowler): https://martinfowler.com/bliki/CircuitBreaker.html
- Exponential Backoff & Jitter (AWS Architecture Blog): https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/

---

## 🔧 Troubleshooting (Common Issues)

- **UI Port Conflict (4200)**  
  If `prefect server start` complains or the UI is not reachable, bind a custom port:  
  ```bash
  prefect server start --host 127.0.0.1 --port 4300
  ```
  Then open http://127.0.0.1:4300/

- **Worker Queue Mismatch**  
  Error: `QueueNotFound` → Ensure your deployment uses the same queue/tag as your worker.  
  Example: deployment tagged with `["week-10"]` → start worker with:  
  ```bash
  prefect worker start -p process -q week-10
  ```

- **API URL Differences**  
  Local default: `http://127.0.0.1:4200/api`.  
  Prefect Cloud: `https://api.prefect.cloud/api/accounts/<id>/workspaces/<id>` (switch via `prefect cloud login`).

- **Missing Packages (`ModuleNotFoundError`)**  
  Verify your venv is active. Re‑install:  
  ```bash
  pip install -r env/requirements.txt
  ```

- **Deployment Not Running**  
  Ensure both the server (UI/API) and a worker are running. Without a worker process, schedules won’t execute.

- **Stale State / Orphan Runs**  
  Restart server + worker to clear stuck runs. Delete the `.prefect/` folder if corruption is suspected.

