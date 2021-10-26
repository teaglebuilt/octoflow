from airflow.models import DAG
from airflow.decorators import task

from datetime import datetime

with DAG('dag', schedule_interval='@daily', 
         start_date=datetime(2020, 1, 1), catchup=False) as dag:

    @task.docker(
        image="quay.io/bitnami/python:3.9",
        network_mode="bridge",
        api_version="auto",
    )
    def f():
        import random

        return [random.random() for _ in range(100)]