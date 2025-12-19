from airflow import DAG 
import pendulum 
import datetime 
from airflow.operators.python import PythonOperator 
from plugins.common.common_func import regist2  

with DAG(
    dag_id = "dags_pyton_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025,12,18, tz= 'Asia/Seoul'),
    catchup = False
) as dag:

    regist2_t1 = PythonOperator(
        task_id = 'regist2_t1',
        python_callable=regist2,
        op_args= ['jkkim','man','kr','seoul'],
        op_kwargs={'email':'jkkim@gmail.com', 'phone':'010-0000-0000'}
    )

    regist2_t1