import boto3

# Do not hard code credentials
s3 = boto3.client(
    's3',
    region_name='cn-north-1',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='AKIA3NC37QVN3WCEFJGR',
    aws_secret_access_key='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'
)

bucket = 'pgiot-s3-test/'
constant1 = 'efd/'
group = 'group001/'
year = '2019/'
month = '12/'
date = '24/'

#response = s3.upload_file('test.jpg', 'pgiot-s3-test', 'test.jpg')
response = s3.upload_file('test.jpg', 'pgiot-s3-test', constant1 + group + year + month + date + 'test1.jpg')
#response = s3.list_buckets()

# Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
    # print(f'  {bucket["Name"]}')

# Let's use Amazon S3
#s3 = boto3.resource('s3')


# Print out bucket names
# for bucket in s3.buckets.all():
    # print(bucket.name)

# Upload a new file
# data = open('test.jpg', 'rb')
# client.Bucket('pgiot-s3-test').put_object(Key='test.jpg', Body=data)