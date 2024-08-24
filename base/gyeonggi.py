import requests
import os
import re
from dotenv import load_dotenv
from s3_method import upload_s3_bucket

load_dotenv()

ENTERPRISE_NAME = ''
pIndex = 1
pSize = 10

def fetch_data():
    url = f"{os.getenv('GYEONGGI_URL')}?KEY={os.getenv('GYEONGGI_API_KEY')}&Type=json&ENTRPRS_NM={ENTERPRISE_NAME}&pIndex={pIndex}&pSize={pSize}"
    response = requests.get(url).json()
    data = response['GGJOBABARECRUSTM'][1]['row']
    
    # 날짜 형식 변환
    date_pattern = re.compile(r'^(\d{4})(\d{2})(\d{2})$')
    
    for item in data:
        if 'RCPT_END_DE' in item:
            date_str = item['RCPT_END_DE']
            match = date_pattern.match(date_str)

            # 20240822 -> 2024-08-22, %Y%m%d -> %Y-%m-%d 형식으로 변환
            if match:
                item['RCPT_END_DE'] = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

    print(f"data length: {len(data)}")
    return data

if __name__ == "__main__":
    filename = 'gyeonggi_original_data.json'
    data = fetch_data()
    #upload_s3_bucket(data, filename)