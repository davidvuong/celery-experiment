import time
import random
from celery import Celery

# see: http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

@app.task
def add_and_sleep(x, y):
    result = x + y
    time.sleep(random.randint(1, 3))
    return result

# see: http://docs.celeryproject.org/en/latest/userguide/signals.html
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # see: http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
    sender.add_periodic_task(10, add.s(1, 1), name='add_every_10s')
    sender.add_periodic_task(2, add_and_sleep.s(2, 2), name='add_and_sleep_every_2s')
