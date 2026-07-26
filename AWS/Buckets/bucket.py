import os
import boto3
from dotenv import load_dotenv

load_dotenv()

aws_key=os.getenv("AWS_ACCESS_KEY_ID")
aws_secrate=os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region=os.getenv("AWS_REGION")

session = boto3.Session(
    aws_access_key_id=aws_key,
    aws_secret_access_key=aws_secrate,
    region_name=aws_region,
)

sts = session.client("sts")
s3 = session.client("s3")

# identity = sts.get_caller_identity()

# print(f"Account ID: {identity['Account']}")
# print(f"User/Role: {identity['Arn']}")
BUCKET_NAME='bucket-seq-1'

# s3.create_bucket(
#     Bucket=BUCKET_NAME,
#     CreateBucketConfiguration={"LocationConstraint": aws_region}
# )

# s3.upload_file("text-bucket.json", BUCKET_NAME, "text-bucket.json")
s3.upload_file("index.html", BUCKET_NAME, "index.html")
# s3.delete_object(Bucket=BUCKET_NAME, Key="text-bucket.txt")

# s3.delete_bucket(Bucket=BUCKET_NAME)

# response = s3.list_buckets()

# for bucket in response["Buckets"]:
#     print(bucket["Name"])