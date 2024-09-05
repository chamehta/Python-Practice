from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

doc_md = """this dag shows the context of a dag run"""

default_args = {
    'start_date': datetime(2020, 1, 1)
}


def _my_function(**context):
    print(context)


with DAG('l01_context_object', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    my_task = PythonOperator(
        task_id='my_task',
        python_callable=_my_function
    )
