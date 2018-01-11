from celery import Celery

app = Celery('tasks',
             backend='redis://redis:6379/2',
             broker='redis://redis:6379/2')

@app.task
def add(x, y):
    return x + y
