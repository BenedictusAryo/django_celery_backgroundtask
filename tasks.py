from celery import Celery
from time import sleep


# app = Celery('tasks', broker='localhost')
app = Celery('tasks', broker='amqp://django:django@192.168.0.117')
# app = Celery('tasks', broker='localhost')

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]