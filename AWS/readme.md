# AWS SDK for Python (boto3) - Ubuntu Setup Guide

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [Common AWS Operations](#common-aws-operations)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Overview

Boto3 is the Amazon Web Services (AWS) SDK for Python. It allows Python developers to write software that uses AWS services like Amazon S3, EC2, DynamoDB, and more.

**Supported Services:** S3, EC2, RDS, DynamoDB, Lambda, SNS, SQS, CloudWatch, IAM, and 200+ more AWS services.

---

## Prerequisites

- Ubuntu 20.04 LTS or later
- Python 3.7 or higher
- AWS Account with access credentials
- pip (Python package manager)

**Check your Python version:**
```bash
python3 --version
```

---

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
pip3 install boto3
```

### 4. Verify Installation
```bash
python3 -c "import boto3; print(boto3.__version__)"
```

### 5. Install Additional Tools (Optional)
```bash
pip3 install botocore awscli
```

---

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

---

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

---

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

**Upload File:**
```python
s3.upload_file('local_file.txt', 'my-bucket', 's3_key.txt')
```

**Download File:**
```python
s3.download_file('my-bucket', 's3_key.txt', 'local_file.txt')
```

**List Objects in Bucket:**
```python
response = s3.list_objects_v2(Bucket='my-bucket')
for obj in response.get('Contents', []):
    print(obj['Key'])
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

---

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

---

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

---

## Useful Commands

| Command | Purpose |
|---------|---------|
| `pip3 install boto3` | Install boto3 |
| `pip3 install boto3 --upgrade` | Upgrade boto3 |
| `pip3 freeze \| grep boto3` | Check installed version |
| `aws configure` | Configure AWS credentials (requires awscli) |
| `aws s3 ls` | List S3 buckets |
| `python3 script.py` | Run Python script with boto3 |

---

## Resources

- [AWS boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS SDK for Python GitHub](https://github.com/boto/boto3)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/)
- [boto3 Examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python)

---

## License

This guide is provided as-is for educational purposes.
