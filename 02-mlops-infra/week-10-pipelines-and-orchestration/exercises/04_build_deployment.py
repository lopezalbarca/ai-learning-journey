from __future__ import annotations
from pathlib import Path
import importlib.util

from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

# Dynamically load daily_job from sibling file '04_scheduling.py'
mod_path = Path(__file__).with_name("04_scheduling.py")
spec = importlib.util.spec_from_file_location("schedule_mod", mod_path)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
daily_job = getattr(module, "daily_job")

if __name__ == "__main__":
    deployment = Deployment.build_from_flow(
        flow=daily_job,
        name="daily-0900",
        schedule=CronSchedule(cron="0 9 * * *", timezone="Europe/Madrid"),
        tags=["week-10"],
        parameters={},
    )
    deployment.apply()
    print("Deployment created. Start an agent/worker to execute on schedule.")
