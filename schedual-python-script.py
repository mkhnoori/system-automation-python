import schedule
import time

def task():
    print("Running scheduled task!")

schedule.every().day.at("03:00").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
