import boto3
import datetime
import time
constant1 = 'efd/' 

def s3_init(region, access_key, secret_key):
    
    s3 = boto3.client(
    's3',
    region_name=region,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
    )
    return s3

 
def s3_upload(filepath, group, client):
    now_time = datetime.datetime.now()
    year = now_time.strftime("%Y")
    month = now_time.strftime("%m")
    date = now_time.strftime("%d")
    name = filepath
    response = client.upload_file(filepath, 'pgiot-s3-test', constant1 + group + '/' + year + '/' + month + '/' + date + '/' + name, ExtraArgs={'ACL': 'public-read'})
