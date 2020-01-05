import boto3
constant1 = 'efd/' 

def s3_init():
    # Do not hard code credentials
    s3 = boto3.client(
    's3',
    region_name='cn-north-1',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='AKIA3NC37QVN3WCEFJGR',
    aws_secret_access_key='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'
    )
    return s3

 
def s3_upload(filepath, group, year, month, date, name, client):
    response = client.upload_file(filepath, 'pgiot-s3-test', constant1 + group + '/' + year + '/' + month + '/' + date + '/' + name, ExtraArgs={'ACL': 'public-read'})
