from airflow import DAG 
import pendulum 
import datetime 
from airflow.operators.email import EmailOperator 

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * * *",
    start_date=pendulum.datetime(2025,12,18, tz='Asia/Seoul'),
    catchup=False
) as dag:

    send_email_task = EmailOperator(
        task_id="send_email_task",
        to="galaxy1022@naver.com",
        cc="venusgalaxy1022@gmail.com"
        subject="Airflow Email Test",
        html_content="<h1> Airflow 작업이 완료되었습니다 </h1>"
    )