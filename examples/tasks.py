from celery import shared_task

from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    print('sleepy done')
    return None 