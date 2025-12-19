from airflow import DAG 
import datetime
import pendulum 
from airflow.operators.python import PythonOperator
import random # 랜덤값을 불러오는 라이브러리


# task 1개만 돌리는 것
with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025,12,18, tz='Asia/Seoul'),
    catchup=False
 ) as dag:
    def select_fruit():  # 함수가 필요함. 정의된 함수는 들여쓰기 내애 있어야 함 
        fruit = ['APPLE','BANANA','ORANGE','AVOCADO']
        rand_int = random.randint(0,3) # 0~3까지 임의의 수를 리턴하겠음. 
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable = select_fruit      # 어떤 함수를 실행시킬 것이냐
    )
    
    py_t1
        







