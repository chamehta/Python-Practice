from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

doc_md = """this dag shows the context of a dag run"""

default_args = {
    'start_date': datetime(2021, 1, 1)
}


with DAG('l02_bash_operator', schedule_interval='@daily', default_args=default_args) as dag:
    execute_command = BashOperator(
        task_id='execute_command',
        bash_command="scripts/commands.sh",
        do_xcom_push=False,
        env={"MY_VAR": "MY_VALUE"},
        skip_exit_code=10
    )
