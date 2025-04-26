import boto3
import os

s3 = boto3.client('s3', 
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

bucket_name = 'fintech-batch-data-6d065094'  
file_name = '/opt/airflow/data/card_transactions.csv'
s3_key = 'raw/card_transactions.csv'  

s3.upload_file(file_name, bucket_name, s3_key)

print(f"{file_name} 파일을 S3 버킷 {bucket_name}/{s3_key} 경로에 업로드했습니다")