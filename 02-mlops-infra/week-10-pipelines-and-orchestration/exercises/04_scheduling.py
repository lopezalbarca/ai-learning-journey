from __future__ import annotations
from prefect import flow

@flow
def daily_job():
    # Put your end-to-end pipeline here (e.g., import and call etl())
    return "ok"

if __name__ == "__main__":
    print(daily_job())
