# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
import warnings
warnings.warn(
    "This module is deprecated. Please use airflow.operators.dummy.", DeprecationWarning, stacklevel=2
)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'retries': 0
}

dag = DAG(dag_id='DAG-1', default_args=default_args, catchup=False, schedule_interval='@once')

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end
