from celery import shared_task
import time

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

    # celery -A d5 worker -l INFO