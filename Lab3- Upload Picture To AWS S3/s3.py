import boto3
constant1 = 'efd/' 

def s3_init(region, access_key, secret_key):
    # Do not hard code credentials
    s3 = boto3.client(
    's3',
    region_name=region,
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
    )
    return s3

 
def s3_upload(filepath, group, year, month, date, name, client):
    response = client.upload_file(filepath, 'pgiot-s3-test', constant1 + group + '/' + year + '/' + month + '/' + date + '/' + name, ExtraArgs={'ACL': 'public-read'})
