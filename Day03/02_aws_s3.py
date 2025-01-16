import boto3 # type: ignore

s3 = boto3.resource('s3')

def show_all_bucket():
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload_to_bucket(s3,filename,bucket_name,source_path):
    try:
        data = open(source_path,'rb')
        s3.Bucket(bucket_name).put_object(Key=filename, Body=data)
        print("Backup stored to s3")
    except Exception as e:
        print("Backup not stored to s3\nError :",e)

filename = "backup1_2025-01-08.tar.gz"
bucket_name = "pythonfordevops"
source_path = "D:/DevOps/Python-For-Devops/Backup/backup1_2025-01-08.tar.gz"
upload_to_bucket(s3,filename,bucket_name,source_path)
show_all_bucket()