# celery-experiment

## Installation

```bash
# Setup an environment
mkvirtualenv -p python3 celery-experiment

# Install dependencies
pip install -r requirements.txt

# Spin up containers for mock services
docker-compose up

# Run workers
celery --app=tasks worker --loglevel=info

# (optional) Run I/O bounded workers
celery --app=tasks worker --pool=gevent --concurrency=100 --loglevel=info

# Run the scheduler
celery --app=tasks beat --loglevel=info
```

## Flow

In this example, there is a scheduler controlled by celery-beat to trigger a new task every 10s. A worker will pick up the scheduled task and then perform the action.

**NOTE:** This experiment uses Redis as the broker rather than the suggested RabbitMQ.

## Monitoring

https://github.com/mher/flower

```bash
celery flower -A tasks --broker=redis://localhost:6379//
```

## Reading Material

* https://medium.com/the-andela-way/timed-periodic-tasks-in-celery-58c99ecf3f80
* http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
* https://github.com/celery/celery
* https://stackoverflow.com/questions/46517613/python-task-queue-alternatives-and-frameworks
* https://news.ycombinator.com/item?id=15681066
* http://docs.celeryproject.org/en/latest/faq.html
* https://stackoverflow.com/questions/42948547/which-pool-class-should-i-use-prefork-eventlet-or-gevent-in-celery
* https://www.distributedpython.com/2018/10/26/celery-execution-pool/
* https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/
* https://denibertovic.com/posts/celery-best-practices/
* https://news.ycombinator.com/item?id=7909201
* http://docs.celeryproject.org/en/latest/userguide/canvas.html#chains
