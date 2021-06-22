from celery import Celery
from time import sleep

ODBC_DRIVER = 'ODBC Driver 17 for SQL Server'
DB_IP = '192.168.0.117'
DB_NAME = 'test_db_mssql'
USERNAME = 'testuser'
PASSWD = 'testuser'


# app = Celery('tasks', broker='amqp://django:django@172.16.59.242')
app = Celery('tasks', broker='amqp://django:django@192.168.0.117:5672', backend=f'db+mssql+pyodbc://{USERNAME}:{PASSWD}@{DB_IP}/{DB_NAME}?driver={ODBC_DRIVER}')

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]
