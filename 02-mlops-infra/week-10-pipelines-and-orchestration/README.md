# W10 · Pipelines & Orchestration (MLOps & Infra)

**Goal:** Design robust pipelines using a modern orchestrator (we’ll use **Prefect 2** as the primary tool) to handle **scheduling, dependencies, retries, timeouts, backoff, and resilience patterns**. By the end, you’ll be able to ship a small but production‑minded flow that runs on a schedule and survives transient failures.

---

## Learning outcomes
- Model workflows as **flows** and **tasks** with clear dependencies.
- Configure **retries**, **timeouts**, and **exponential backoff** for transient errors.
- Add **circuit‑breaker / fallback** style resilience at the flow level.
- Package a **scheduled deployment** (cron) with environment configuration.
- Log and persist **run metadata** for observability (ids, states, durations).

> Note: We focus on **Prefect 2** for a smooth local developer experience. The same ideas translate to Airflow (DAGs, Operators, Sensors) if you prefer it later.

---

## Prerequisites
- Python **3.11+**
- Basic knowledge from W08–W09 (project structure, environments, logging/metrics mindset).

---

## Plan: Your Step‑by‑Step Guide

### 1) Prepare your lab
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

Base deps this week: `prefect`, `pandas`, `scikit-learn`, `httpx`, `pydantic`.

---

### 2) First flow with dependencies
Create `exercises/01_basic_flow.py`:
```python
from datetime import timedelta
import random
import time

import httpx
from prefect import flow, task
from prefect.states import Failed

@task
def extract() -> dict:
    # Simulate I/O
    time.sleep(0.3)
    return {"items": [1, 2, 3, 4, 5]}

@task
def transform(payload: dict) -> list[int]:
    items = payload["items"]
    return [i * 2 for i in items]

@task
def load(values: list[int]) -> int:
    # Fake sink
    return len(values)

@flow(name="basic-etl")
def etl():
    data = extract()
    doubled = transform(data)
    count = load(doubled)
    return {"count": count}

if __name__ == "__main__":
    print(etl())
```

**What to observe**
- Task dependency graph: `extract -> transform -> load`.
- The **flow** is the orchestration boundary; tasks are units with retries/timeouts later.

---

### 3) Retries, timeouts & backoff
Open `exercises/02_retries_and_timeouts.py`:
```python
from datetime import timedelta
import random
import time

from prefect import flow, task

@task(retries=3, retry_delay_seconds=2, timeout_seconds=10)
def flaky_call() -> int:
    # Emulate a transient failure (e.g., 30% error rate)
    if random.random() < 0.3:
        raise RuntimeError("Transient upstream error")
    time.sleep(0.2)
    return 42

@flow(name="robust-flow")
def robust_flow():
    return flaky_call()

if __name__ == "__main__":
    print(robust_flow())
```

- `retries=3` + `retry_delay_seconds=2` gives basic backoff (you can implement exponential by increasing delay inside the task or chaining small waits).
- `timeout_seconds` prevents hung tasks from blocking forever.

> Tip: For **exponential backoff with jitter**, you can wrap the body with a loop and use `time.sleep(min(max_delay, base * 2**attempt + random.random()))` when catching exceptions.

---

### 4) Resilience patterns (fallbacks & circuit breaker)
Open `exercises/03_resilience_patterns.py`:
```python
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from prefect import flow, task

@dataclass
class Circuit:
    failures: int = 0
    threshold: int = 3
    open_until: Optional[float] = None  # epoch seconds

    def allow(self) -> bool:
        now = time.time()
        if self.open_until and now < self.open_until:
            return False
        return True

    def record_failure(self, cooldown_s: int = 30):
        self.failures += 1
        if self.failures >= self.threshold:
            self.open_until = time.time() + cooldown_s

    def reset(self):
        self.failures = 0
        self.open_until = None

circuit = Circuit(threshold=3)

@task(retries=2, retry_delay_seconds=1)
def primary_provider(q: str) -> str:
    # Pretend this is a remote API that sometimes degrades
    if not circuit.allow():
        raise RuntimeError("Circuit open")
    # Simulate 50% failure
    if hash((q, datetime.utcnow().minute)) % 2 == 0:
        circuit.record_failure(cooldown_s=20)
        raise RuntimeError("Primary provider failure")
    circuit.reset()
    return f"primary:{q}"

@task
def secondary_provider(q: str) -> str:
    # Always works but poorer quality / higher latency
    time.sleep(0.3)
    return f"secondary:{q}"

@flow(name="fallback-with-circuit")
def answer(q: str) -> str:
    try:
        return primary_provider(q)
    except Exception:
        return secondary_provider(q)

if __name__ == "__main__":
    print(answer("hello"))
```

- **Circuit breaker** prevents hammering a failing upstream.
- **Fallback** ensures graceful degradation instead of full failure.

---

### 5) Scheduling the flow (cron)
We’ll ship a scheduled deployment to run daily at **09:00 Europe/Madrid**.

Create `exercises/04_scheduling.py`:
```python
from prefect import flow

@flow
def daily_job():
    # Put your end-to-end pipeline here (e.g., etl())
    return "ok"

if __name__ == "__main__":
    # For local ad-hoc run
    print(daily_job())
```

**Create a deployment with a cron schedule** (example, via Python API):
```python
# file: exercises/04_build_deployment.py
from prefect import flow
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from exercises._04_scheduling import daily_job  # adjust import if needed

if __name__ == "__main__":
    deployment = Deployment.build_from_flow(
        flow=daily_job,
        name="daily-0900",
        schedule=(CronSchedule(cron="0 9 * * *", timezone="Europe/Madrid")),
        tags=["week-10"],
        parameters={},  # if your flow uses parameters
    )
    deployment.apply()
    print("Deployment created. Start an agent to pick it up.")
```

> Run an agent/worker locally so scheduled runs can execute. Check Prefect docs for the agent/worker command in your version. Keep logs on to verify triggers, states, and durations.

---

### 6) Observability checklist
- Log run IDs, start/end times, and states.
- Capture task durations (Prefect UI/CLI already shows this).
- Keep parameters & env in the run metadata (for reproducibility).
- If using external calls, include a **correlation ID** per run for tracing downstream logs.

---

## Deliverables
- `env/requirements.txt` frozen (after installing `env/requirements.base.txt`).
- Runnable examples in `exercises/`:
  - `01_basic_flow.py`
  - `02_retries_and_timeouts.py`
  - `03_resilience_patterns.py`
  - `04_scheduling.py` (+ optional `04_build_deployment.py`)
- A scheduled deployment created (daily cron) and visible in your local UI/CLI.
- Short note (Markdown or CSV) capturing a few run IDs, states, and durations.

---

## Folder layout (Week 10)
```
02-mlops-infra/
  week-10-pipelines-and-orchestration/
    README.md
    CHECKLIST.md
    .gitignore
    env/
      setup.ps1
      setup.sh
      requirements.base.txt
      requirements.txt
    resources/
      links.md
    exercises/
      01_basic_flow.py
      02_retries_and_timeouts.py
      03_resilience_patterns.py
      04_scheduling.py
      04_build_deployment.py
      04_conceptual_questions.md
```
