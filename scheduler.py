from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_pipeline
from config import SCHEDULE_HOURE, SCHEDULE_MINUTE, TIME_ZONE
scheduler = BlockingScheduler()

scheduler.add_job(run_pipeline, trigger="cron", hour=SCHEDULE_HOURE, minute=SCHEDULE_MINUTE, timezone=TIME_ZONE)

print('scheduler started....')
print(f'the scheduler will start at {SCHEDULE_HOURE}:{SCHEDULE_MINUTE}')
if __name__ == "__main__":
    scheduler.start()

