import boto3
import os
import dotenv

dotenv.load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

s3 = boto3.resource('s3',aws_access_key_id=access_key,aws_secret_access_key=secret_key,region_name='ap-south-1')

# for bucket in s3.buckets.all():
#     print(bucket.name)

# create new bucket
bucket_name = 'dev-ism-bucket-3'  # Ensure this name is globally unique
s3.create_bucket(
    Bucket=bucket_name, 
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    })

for bucket in s3.buckets.all():
    print(f"Created bucket: {bucket.name}")


# delete bucket
# bucket_name = 'my-new-bucket-ismail'
# s3.Bucket(bucket_name).delete()

# delete multiple buckets
# for bucket in s3.buckets.all():
#     bucket.objects.all().delete()
#     #  Delete all versions (if versioning enabled)
#     bucket.object_versions.all().delete()
#     bucket.delete()

#     print(f"Deleted bucket: {bucket.name}")