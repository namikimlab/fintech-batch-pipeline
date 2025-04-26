from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 1),
}

with DAG('fintech_batch_pipeline',
         default_args=default_args,
         schedule_interval=None, 
         catchup=False) as dag:

    # 1. Create data 
    generate_data = BashOperator(
        task_id='generate_data',
        bash_command='python /opt/airflow/scripts/generate_transactions.py'
    )

    # 2. S3 upload
    upload_to_s3 = BashOperator(
        task_id='upload_to_s3',
        bash_command='python /opt/airflow/scripts/upload_to_s3.py',
        env={
        'AWS_ACCESS_KEY_ID': '{{ var.value.AWS_ACCESS_KEY_ID }}',
        'AWS_SECRET_ACCESS_KEY': '{{ var.value.AWS_SECRET_ACCESS_KEY }}'
        }
    )

    # 3. Spark ETL 
    spark_etl = DockerOperator(
        task_id='spark_etl',
        image='bitnami/spark:latest',
        api_version='auto',
        auto_remove=True,
        command='spark-submit /opt/airflow/scripts/spark_etl.py',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        environment={
            'AWS_ACCESS_KEY_ID': '{{ var.value.AWS_ACCESS_KEY_ID }}',
            'AWS_SECRET_ACCESS_KEY': '{{ var.value.AWS_SECRET_ACCESS_KEY }}'
        },
        mounts=[
            Mount(
                type='bind',
                source='/Users/apple/2025/fintech-batch-pipeline/scripts',
                target='/opt/airflow/scripts'
            ),
            Mount(
                type='bind',
                source='/var/run/docker.sock',
                target='/var/run/docker.sock'
            )
        ]
    )

    generate_data >> upload_to_s3 >> spark_etl
