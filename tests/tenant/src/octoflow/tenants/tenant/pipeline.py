from airflow.models.dag import dag
from airflow.utils.dates import days_ago
from airflow.operators.dummy import DummyOperator


@dag(start_date=days_ago(2))
def generate_dag():
    op = DummyOperator(task_id="task")

dag = generate_dag()
