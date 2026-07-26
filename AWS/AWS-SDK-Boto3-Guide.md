# AWS SDK for Python (boto3) - Setup & Operations Guide

> 📘 **Companion guide:** For AWS concepts, the Console, and the AWS CLI (installing/configuring `aws configure`, per-service deep dives, architecture, interview prep), see **[AWS-Learning-Guide.md](./AWS-Learning-Guide.md)**. This guide focuses specifically on scripting AWS with **Python + boto3**.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [Common AWS Operations](#common-aws-operations)
  - [S3 Operations](#s3-operations)
  - [EC2 Operations](#ec2-operations)
  - [IAM Operations](#iam-operations)
  - [DynamoDB Operations](#dynamodb-operations)
  - [Lambda Operations](#lambda-operations)
  - [CloudWatch Operations](#cloudwatch-operations)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Overview

Boto3 is the Amazon Web Services (AWS) SDK for Python. It allows Python developers to write software that uses AWS services like Amazon S3, EC2, DynamoDB, and more.

**Supported Services:** S3, EC2, RDS, DynamoDB, Lambda, SNS, SQS, CloudWatch, IAM, and 200+ more AWS services.

## Prerequisites

- Ubuntu 20.04 LTS or later
- Python 3.7 or higher
- AWS Account with access credentials
- pip (Python package manager)

**Check your Python version:**

```bash
python3 --version
```

## Installation

### 1. Update Ubuntu Packages

```bash
sudo apt-get update
sudo apt-get upgrade -y
```

### 2. Install Python and pip (if not already installed)

```bash
sudo apt-get install python3 python3-pip -y
```

### 3. Install boto3

```bash
sudo apt update
sudo apt install python3-boto3 -y
```

### 4. Verify Installation

```bash
python3 -c "import boto3; print(boto3.__version__)"
```

### 5. Install Additional Tools (Optional)

```bash
pip3 install botocore awscli
```

## Configuration

### Method 1: AWS Configuration File (Recommended)

1. **Create AWS credentials directory:**

   ```bash
   mkdir -p ~/.aws
   ```

2. **Create credentials file:**

   ```bash
   nano ~/.aws/credentials
   ```

   **Add your credentials:**

   ```
   [default]
   aws_access_key_id = YOUR_ACCESS_KEY
   aws_secret_access_key = YOUR_SECRET_KEY

   [profile-name]
   aws_access_key_id = YOUR_ACCESS_KEY
   aws_secret_access_key = YOUR_SECRET_KEY
   ```

3. **Create config file:**

   ```bash
   nano ~/.aws/config
   ```

   **Add your region settings:**

   ```
   [default]
   region = us-east-1
   output = json

   [profile profile-name]
   region = eu-west-1
   output = json
   ```

4. **Set file permissions:**
   ```bash
   chmod 600 ~/.aws/credentials
   chmod 600 ~/.aws/config
   ```

### Method 2: Environment Variables

```bash
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
export AWS_DEFAULT_REGION="us-east-1"
```

### Method 3: Hard-coded (Not Recommended for Production)

```python
import boto3

session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-east-1'
)
```

## Quick Start

### Initialize boto3 Client

```python
import boto3

# Create S3 client
s3_client = boto3.client('s3', region_name='us-east-1')

# Create EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Create DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
```

### Check AWS Connection

```python
import boto3

try:
    # Test connection with STS
    sts = boto3.client('sts')
    identity = sts.get_caller_identity()
    print(f"Account ID: {identity['Account']}")
    print(f"User/Role: {identity['Arn']}")
    print("✓ AWS connection successful!")
except Exception as e:
    print(f"✗ Connection error: {e}")
```

## Common AWS Operations

### S3 Operations

**List Buckets:**

```python
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
```

## Bucket Operations

**Create Bucket**

```python
s3.create_bucket(
    Bucket="bucket-name",
    CreateBucketConfiguration={"LocationConstraint": "ap-south-1"}
)
```

**List Buckets**

```python
response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(bucket["Name"])
```

**Check Bucket Exists**

```python
s3.head_bucket(Bucket="bucket-name")
```

**Get Bucket Location**

```python
response = s3.get_bucket_location(Bucket="bucket-name")
print(response)
```

**Delete Bucket**

```python
# Bucket must be empty first
s3.delete_bucket(Bucket="bucket-name")
```

**Make Bucket Public (ACL)**

```python
s3.put_bucket_acl(Bucket="bucket-name", ACL="public-read")
```

**Enable Versioning**

```python
s3.put_bucket_versioning(
    Bucket="bucket-name",
    VersioningConfiguration={"Status": "Enabled"}
)
```

**Upload File**

```python
s3.upload_file("local-file.txt", "bucket-name", "remote-file.txt")
```

**Download File**

```python
s3.download_file("bucket-name", "remote-file.txt", "local-file.txt")
```

**List Objects in Bucket**

```python
response = s3.list_objects_v2(Bucket="bucket-name")
for obj in response.get("Contents", []):
    print(obj["Key"])
```

**Read File Content (in memory)**

```python
response = s3.get_object(Bucket="bucket-name", Key="file.txt")
print(response["Body"].read().decode())
```

**Get Object Metadata**

```python
response = s3.head_object(Bucket="bucket-name", Key="file.txt")
print(response)
```

**Delete Object**

```python
s3.delete_object(Bucket="bucket-name", Key="remote-file.txt")
```

**Copy Object (across or within buckets)**

```python
s3.copy_object(
    Bucket="destination-bucket",
    CopySource="source-bucket/file.txt",
    Key="file.txt"
)
```

**Move Object (copy + delete original)**

```python
s3.copy_object(
    Bucket="destination-bucket",
    CopySource="source-bucket/file.txt",
    Key="file.txt"
)
s3.delete_object(Bucket="source-bucket", Key="file.txt")
```

**Rename Object (copy + delete, same bucket)**

```python
s3.copy_object(
    Bucket="bucket-name",
    CopySource="bucket-name/old.txt",
    Key="new.txt"
)
s3.delete_object(Bucket="bucket-name", Key="old.txt")
```

**Generate Presigned URL**

```python
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": "bucket-name", "Key": "file.txt"},
    ExpiresIn=3600
)
print(url)
```

**Folder Operations**

S3 has no real folders — these are just keys ending in `/` or containing `/` as a prefix.

\*\*Create Folder

```python
s3.put_object(Bucket="bucket-name", Key="images/")
```

\*\*Upload Into Folder

```python
s3.upload_file("photo.jpg", "bucket-name", "images/photo.jpg")
```

\*\*Delete Folder

```python
# Folder must be empty
s3.delete_object(Bucket="bucket-name", Key="images/")
```

### EC2 Operations

**List Instances:**

```python
import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
```

**Start Instance:**

```python
ec2.start_instances(InstanceIds=['i-1234567890abcdef0'])
```

**Stop Instance:**

```python
ec2.stop_instances(InstanceIds=['i-1234567890abcdef0'])
```

### IAM Operations

**List Users:**

```python
import boto3

iam = boto3.client('iam')
response = iam.list_users()
for user in response['Users']:
    print(user['UserName'])
```

**Create User:**

```python
iam.create_user(UserName='devops-learner')
```

**Attach a Managed Policy to a User:**

```python
iam.attach_user_policy(
    UserName='devops-learner',
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
)
```

**Create an Access Key:**

```python
response = iam.create_access_key(UserName='devops-learner')
print(response['AccessKey']['AccessKeyId'])
print(response['AccessKey']['SecretAccessKey'])  # shown only once
```

**Create a Role (for EC2/Lambda to assume):**

```python
import json

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {"Service": "ec2.amazonaws.com"},
        "Action": "sts:AssumeRole"
    }]
}

iam.create_role(
    RoleName='EC2-S3-ReadOnly-Role',
    AssumeRolePolicyDocument=json.dumps(trust_policy)
)
iam.attach_role_policy(
    RoleName='EC2-S3-ReadOnly-Role',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)
```

**Confirm Current Identity:**

```python
sts = boto3.client('sts')
identity = sts.get_caller_identity()
print(identity['Account'], identity['Arn'])
```

### DynamoDB Operations

**Create Table:**

```python
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.create_table(
    TableName='my-table',
    KeySchema=[
        {'AttributeName': 'id', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'id', 'AttributeType': 'S'}
    ],
    BillingMode='PAY_PER_REQUEST'
)
```

**Put Item:**

```python
table = dynamodb.Table('my-table')
table.put_item(Item={'id': '123', 'name': 'John'})
```

**Get Item:**

```python
response = table.get_item(Key={'id': '123'})
print(response['Item'])
```

**Scan Table:**

```python
response = table.scan()
for item in response['Items']:
    print(item)
```

### Lambda Operations

**List Functions:**

```python
import boto3

lam = boto3.client('lambda', region_name='us-east-1')
response = lam.list_functions()
for fn in response['Functions']:
    print(fn['FunctionName'], fn['Runtime'])
```

**Invoke a Function:**

```python
import json

response = lam.invoke(
    FunctionName='my-function',
    InvocationType='RequestResponse',  # or 'Event' for async
    Payload=json.dumps({'key': 'value'})
)
result = json.loads(response['Payload'].read())
print(result)
```

**Create a Function (from a zipped deployment package):**

```python
with open('function.zip', 'rb') as f:
    zipped_code = f.read()

lam.create_function(
    FunctionName='my-function',
    Runtime='python3.12',
    Role='arn:aws:iam::123456789012:role/lambda-execution-role',
    Handler='handler.lambda_handler',
    Code={'ZipFile': zipped_code},
    Timeout=30,
    MemorySize=128,
)
```

**Update Function Code:**

```python
with open('function.zip', 'rb') as f:
    lam.update_function_code(FunctionName='my-function', ZipFile=f.read())
```

**Delete a Function:**

```python
lam.delete_function(FunctionName='my-function')
```

### CloudWatch Operations

**Put Metric:**

```python
import boto3

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
cloudwatch.put_metric_data(
    Namespace='MyApp',
    MetricData=[
        {
            'MetricName': 'CustomMetric',
            'Value': 100,
            'Unit': 'Count'
        }
    ]
)
```

**Get Metrics:**

```python
response = cloudwatch.list_metrics(Namespace='MyApp')
for metric in response['Metrics']:
    print(metric['MetricName'])
```

## Best Practices

### 1. Use IAM Roles (for EC2 instances)

Instead of storing credentials, attach IAM roles to EC2 instances:

```python
# boto3 will automatically use the instance's IAM role
import boto3
s3 = boto3.client('s3')
```

### 2. Use Environment Variables

```bash
export AWS_ACCESS_KEY_ID="key"
export AWS_SECRET_ACCESS_KEY="secret"
export AWS_DEFAULT_REGION="us-east-1"
```

### 3. Use Named Profiles

```python
session = boto3.Session(profile_name='dev')
s3 = session.client('s3')
```

### 4. Error Handling

```python
import boto3
from botocore.exceptions import ClientError

try:
    s3 = boto3.client('s3')
    s3.head_bucket(Bucket='my-bucket')
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == '404':
        print("Bucket does not exist")
    else:
        print(f"Error: {e}")
```

### 5. Pagination

```python
import boto3

s3 = boto3.client('s3')
paginator = s3.get_paginator('list_objects_v2')
for page in paginator.paginate(Bucket='my-bucket'):
    for obj in page.get('Contents', []):
        print(obj['Key'])
```

### 6. Use Resource vs Client

- **Client**: Lower-level, more control, matches AWS API exactly
- **Resource**: Higher-level, more Pythonic, easier to use

```python
# Client approach
s3_client = boto3.client('s3')
s3_client.put_object(Bucket='bucket', Key='key', Body=b'data')

# Resource approach
s3 = boto3.resource('s3')
bucket = s3.Bucket('bucket')
bucket.put_object(Key='key', Body=b'data')
```

## Troubleshooting

### Issue: "NoCredentialsError"

**Solution:** Ensure credentials are properly configured:

```bash
# Check if credentials file exists
cat ~/.aws/credentials

# Or set environment variables
export AWS_ACCESS_KEY_ID="your_key"
export AWS_SECRET_ACCESS_KEY="your_secret"
```

### Issue: "Unable to locate credentials"

**Solution:** Check credential file permissions:

```bash
chmod 600 ~/.aws/credentials
chmod 600 ~/.aws/config
```

### Issue: "RegionNotSpecified"

**Solution:** Set default region:

```bash
export AWS_DEFAULT_REGION="us-east-1"
```

Or in code:

```python
boto3.client('s3', region_name='us-east-1')
```

### Issue: "AccessDenied" Error

**Solution:** Verify IAM permissions for your user/role. Check IAM policy:

```bash
aws iam get-user-policy --user-name your-user --policy-name policy-name
```

### Enable Debug Logging

```python
import boto3
import logging

logging.basicConfig(level=logging.DEBUG)
boto3.set_stream_logger('', logging.DEBUG)

# Your boto3 code here
```

## Useful Commands

| Command                        | Purpose                                     |
| ------------------------------ | ------------------------------------------- |
| `pip3 install boto3`           | Install boto3                               |
| `pip3 install boto3 --upgrade` | Upgrade boto3                               |
| `pip3 freeze \| grep boto3`    | Check installed version                     |
| `aws configure`                | Configure AWS credentials (requires awscli) |
| `aws s3 ls`                    | List S3 buckets                             |
| `python3 script.py`            | Run Python script with boto3                |

## Resources

- [AWS boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS SDK for Python GitHub](https://github.com/boto/boto3)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/)
- [boto3 Examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python)

## License

This guide is provided as-is for educational purposes.
