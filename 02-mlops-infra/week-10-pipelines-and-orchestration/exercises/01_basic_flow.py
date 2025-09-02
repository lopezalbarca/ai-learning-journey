from __future__ import annotations
import time
from prefect import flow, task

@task
def extract() -> dict:
    time.sleep(0.3)
    return {"items": [1, 2, 3, 4, 5]}

@task
def transform(payload: dict) -> list[int]:
    return [i * 2 for i in payload["items"]]

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
