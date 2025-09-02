from __future__ import annotations
import csv
import time
from datetime import datetime
from pathlib import Path

# Import the flow(s)
try:
    # Prefer daily job if present
    from ._04_scheduling import daily_job  # type: ignore
except Exception:
    daily_job = None

from ._01_basic_flow import etl  # type: ignore

RUNS_PATH = Path(__file__).resolve().parents[1] / "runs" / "metrics.csv"

def _append(row: dict) -> None:
    RUNS_PATH.parent.mkdir(parents=True, exist_ok=True)
    file_exists = RUNS_PATH.exists()
    with RUNS_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp","flow","state","duration_ms","notes"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

def run_and_log(flow_callable, flow_name: str, notes: str = "") -> None:
    start = time.time()
    state = "success"
    try:
        flow_callable()
    except Exception as ex:
        state = f"error:{type(ex).__name__}"
    finally:
        duration_ms = int((time.time() - start) * 1000)
        _append({
            "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "flow": flow_name,
            "state": state,
            "duration_ms": duration_ms,
            "notes": notes,
        })
        print(f"[{flow_name}] {state} in {duration_ms} ms → logged to {RUNS_PATH}")

if __name__ == "__main__":
    if daily_job is not None:
        run_and_log(daily_job, "daily_job", notes="adhoc")
    run_and_log(etl, "etl", notes="adhoc")
