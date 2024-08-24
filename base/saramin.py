import requests
import os
from typing import List
from dotenv import load_dotenv
from s3_method import upload_s3_bucket

load_dotenv()

COUNT = 110     # 공고 건수
START = 0     # 어디서부터 시작할건지
JOB_CODE = 2    # IT 개발 데이터 직무 코드
LOC_CD = 101000   # 지역코드

def fetch_data() -> List:
    url = f"{os.getenv('SARAMIN_URL')}?access-key={os.getenv('SARAMIN_API_KEY')}&job_type=&edu_lv=&count={COUNT}&start={START}&job_mid_cd={JOB_CODE}&loc_cd={LOC_CD}"
    response = requests.get(url).json()
    data: list = response['jobs']['job']
    
    return data

if __name__ == '__main__':
    filename = 'saramin_original_data.json'
    data = fetch_data()
    #upload_s3_bucket(data, filename)