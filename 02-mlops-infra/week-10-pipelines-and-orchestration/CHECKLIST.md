# W10 · Checklist

### Setup
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

### Observability
- [ ] Run IDs, states, and durations captured (UI/CLI or custom log).
- [ ] Parameters and environment captured for reproducibility.

### Consolidation
- [ ] `04_conceptual_questions.md` answered:
  - What is the difference between a flow and a task?
  - When are retries harmful?
  - How would you implement graceful degradation?
  - Pros/cons of cron scheduling vs event‑driven triggers.
