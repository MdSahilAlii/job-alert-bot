import schedule
import time
from main import run_job

schedule.every().day.at("07:00").do(run_job)

while True:
    schedule.run_pending()
    time.sleep(60)
