import requests
import os
from typing import List, Dict
from dotenv import load_dotenv
from s3_method import upload_s3_bucket

load_dotenv()

NUM_OF_ROWS = 500  # 한 page에 포함된 결과 수
ON_GOING = 'Y'  # 모집 중인 공고만 조회
PAGE_NO = 1  # Page 번호

def fetch_data():
    url = f"{os.getenv('PUBLIC_INSTITUTION_URL')}list?serviceKey={os.getenv('PUBLIC_INSTITUTION_API_KEY')}&resultType=json&numOfRows={NUM_OF_ROWS}&ongoing={ON_GOING}&pageNo={PAGE_NO}"
    response = requests.get(url)
    data = response.json()
    data_list: List[Dict[str]] = data.get('result', [])
    print(f"data length: {len(data_list)}")

    return data_list

if __name__ == '__main__':
    filename = 'public_institution_original_data.json'
    data = fetch_data()
    #upload_s3_bucket(data, filename)
