from __future__ import annotations
import random
import time
from prefect import flow, task

@task(retries=3, retry_delay_seconds=2, timeout_seconds=10)
def flaky_call() -> int:
    if random.random() < 0.3:
        raise RuntimeError("Transient upstream error")
    time.sleep(0.2)
    return 42

@flow(name="robust-flow")
def robust_flow():
    return flaky_call()

if __name__ == "__main__":
    print(robust_flow())
