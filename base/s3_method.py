import json
import os
import boto3
from typing import List
from dotenv import load_dotenv

load_dotenv()   # .env 파일 로드

# S3 클라이언트 생성
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def upload_s3_bucket(data: List, filename: str):
    """
    S3 버킷에 데이터를 업로드하는 함수

    :param data: 업로드할 딕셔너리 데이터
    :param filename: 파일 명
    :return: None
    """
    s3_client.put_object(
        Bucket=os.getenv('S3_BUCKET_NAME'),
        Key=filename,
        Body=json.dumps(data, ensure_ascii=False),
        ContentType = 'application/json'
    )
