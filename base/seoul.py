import requests
import os
from dotenv import load_dotenv
from s3_method import upload_s3_bucket

load_dotenv()

TYPE = 'json'
SERVICE = 'GetJobInfo'
END_INDEX = 10

def fetch_data():
    url = f"{os.getenv('SEOUL_URL')}/{os.getenv('SEOUL_API_KEY')}/{TYPE}/{SERVICE}/1/{END_INDEX}/"
    response = requests.get(url).json()
    data = response['GetJobInfo']['row']
    print(f"data length: {len(data)}")

    return data

if __name__ == '__main__':
    filename = 'seoul_original_data.json'
    data = fetch_data()
    #upload_s3_bucket(data, filename)