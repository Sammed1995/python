""""
This script is for create s3 backet andtake a backup form local to s3
boto3 -> used to do aws task from python
pip install boto3
create aws cli to coneect
aws config
"""

import boto3 # type: ignore
s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(bucket=bucket_name,CreateBucketConfiguration={
                    'LocationConstraint': region})
    print("created bucket succesfully")

bucket_name = "  "
region ="   "


def upload_backup(s3,file,bucket_name,key_name):
    data = open(file_name,'rb')
    s3.bucket(bucket_name).put_object(key=key_name,body=data)

file_name= "  "
upload_backup(s3,file_name,bucket_name,"my_bucket.tar,gz")

create_bucket(s3,bucket_name,region)
show_buckets(s3)