from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

app = FastAPI()

# APScheduler is a popular library for scheduling jobs in Python.
def my_scheduled_job():
    print(f"Task executed at {datetime.datetime.now()}")

@app.get("/scheduler")
def search_items():

    # Initialize scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_scheduled_job, 'interval', seconds=5)  # Every 5 seconds
    scheduler.start()
    return {"Status" : "Scheduler Triggered"}

