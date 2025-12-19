from airflow import DAG 
import pendulum 
import datetime 
from airflow.operator.python import PythonOperator 
from plugins.common.common_func import regist  

with DAG(
    dag_id = "dags_pyton_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025,12,18, tz= 'Asia/Seoul'),
    catchup = False
) as dag:

    regist_t1 = PythonOperator(
        task_id = 'regist_t1',
        python_callable=regist,
        op_args= ['jkkim','man','kr','seoul']

    )

    regist_t1