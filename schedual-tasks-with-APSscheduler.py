from apscheduler.schedulers.background import BackgroundScheduler
import time

def job():
    print("Scheduled job running!")

scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=10)
scheduler.start()

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
