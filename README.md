# Comprehensive AWS Learning Guide: Beginner to Advanced

## Table of Contents
1. [Introduction](#introduction)
2. [Learning Roadmap Timeline](#learning-roadmap-timeline)
3. [AWS Services Overview](#aws-services-overview)
4. [Service Guides](#service-guides)
5. [Best Practices](#best-practices)
6. [DevOps Career Tips](#devops-career-tips)
7. [Final Deployment Project](#final-deployment-project)

---

## Introduction

Amazon Web Services (AWS) is the world's most comprehensive cloud platform, offering over 200 fully featured services from data centers globally. This guide will take you from zero knowledge to AWS proficiency, covering essential services used by enterprises worldwide.

### Why Learn AWS?
- **Market Demand**: AWS skills are highly sought after in the job market
- **Career Growth**: AWS certification holders earn 15-20% more than average IT professionals
- **Real-World Application**: Used by Netflix, Airbnb, Spotify, and millions of other companies
- **Cost Efficiency**: Learn to build scalable infrastructure at a fraction of traditional costs

---

## Learning Roadmap Timeline

### Month 1-2: Foundations (EC2, S3, IAM, VPC)
- Understand cloud computing basics
- Launch and manage EC2 instances
- Store and retrieve data with S3
- Implement secure access with IAM
- Network your resources with VPC

### Month 3: Storage & Database (RDS)
- Set up relational databases
- Understand database backups and replication
- Learn query optimization

### Month 4: Load Balancing & Scaling (ELB, Auto Scaling)
- Distribute traffic across instances
- Implement auto-scaling policies
- Achieve high availability

### Month 5: Monitoring & Logging (CloudWatch)
- Monitor resource performance
- Set up alerts and dashboards
- Analyze logs effectively

### Month 6-7: Serverless & Containers (Lambda, ECS, EKS)
- Deploy serverless functions
- Containerize applications
- Orchestrate containers at scale

### Month 8: CI/CD & DevOps (CodePipeline)
- Automate deployment pipelines
- Implement continuous integration
- Practice DevOps best practices

---

## AWS Services Overview

| Service | Purpose | Best For |
|---------|---------|----------|
| EC2 | Virtual servers in the cloud | Traditional applications, control |
| S3 | Object storage | Files, backups, data lakes |
| IAM | Identity & access management | Security, user management |
| VPC | Isolated network | Network isolation, security |
| RDS | Managed relational database | SQL databases, ACID compliance |
| ELB | Load balancing | Distributing traffic |
| Auto Scaling | Automatic scaling | Cost optimization, elasticity |
| CloudWatch | Monitoring & logging | Metrics, alarms, troubleshooting |
| Lambda | Serverless compute | Event-driven, low-cost processing |
| ECS | Container orchestration | Docker container management |
| EKS | Kubernetes on AWS | Kubernetes orchestration |
| CodePipeline | CI/CD automation | Automated deployments |

---

## Service Guides

## 1. Amazon EC2 (Elastic Compute Cloud)

### What is EC2?
EC2 is AWS's virtual server service that allows you to rent computing capacity in the cloud. Instead of buying physical servers, you can instantly launch virtual servers called "instances" and scale them up or down based on demand.

### Why Use EC2?
**Real-World Example**: Netflix uses thousands of EC2 instances to stream videos to millions of users worldwide. Instead of building data centers, they elastically scale instances based on viewership patterns.

**Advantages**:
- Pay only for what you use
- Resize instances at any time
- Use pre-configured machine images (AMI)
- Access from anywhere via SSH/RDP

### Key Concepts

**Instance Types**:
```
- t2/t3: Burstable performance (dev, testing)
- m5/m6: General purpose (balanced workloads)
- c5/c6: Compute optimized (high-performance)
- r5/r6: Memory optimized (databases, caches)
- i3/i4: Storage optimized (data warehouses)
```

**Instance States**:
- Running: Instance is active and running
- Stopped: Instance is stopped but not terminated
- Terminated: Instance is deleted permanently
- Pending: Instance is starting up
- Stopping: Instance is shutting down

**AMI (Amazon Machine Image)**:
- Pre-configured template for instances
- Contains OS, software, and configurations
- Can be created from existing instances

**Security Groups**:
- Virtual firewall controlling inbound/outbound traffic
- Define rules based on protocol and port
- Act as stateful firewall

### Step-by-Step Setup Guide

#### Step 1: Create a Security Group
```bash
# Using AWS CLI
aws ec2 create-security-group \
  --group-name my-sg \
  --description "My security group"

# Add inbound rule for SSH (port 22)
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxxxxxx \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0
```

#### Step 2: Create a Key Pair
```bash
# Generate key pair
aws ec2 create-key-pair \
  --key-name my-key \
  --output text > my-key.pem

# Set correct permissions
chmod 400 my-key.pem
```

#### Step 3: Launch an Instance
```bash
# Launch t2.micro instance (free tier eligible)
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name my-key \
  --security-groups my-sg
```

#### Step 4: Connect to Instance
```bash
# Connect via SSH
ssh -i my-key.pem ec2-user@<public-ip>

# Update system packages
sudo yum update -y

# Install Apache web server
sudo yum install httpd -y
sudo systemctl start httpd
```

#### Step 5: Create AMI from Instance
```bash
# Create image from running instance
aws ec2 create-image \
  --instance-id i-xxxxxxxxx \
  --name "my-custom-ami" \
  --description "Custom AMI with Apache"
```

### Important Commands

```bash
# List instances
aws ec2 describe-instances

# Start instance
aws ec2 start-instances --instance-ids i-xxxxxxxxx

# Stop instance
aws ec2 stop-instances --instance-ids i-xxxxxxxxx

# Terminate instance
aws ec2 terminate-instances --instance-ids i-xxxxxxxxx

# Describe security groups
aws ec2 describe-security-groups

# Modify security group
aws ec2 revoke-security-group-ingress --group-id sg-xxxxx --protocol tcp --port 22 --cidr 0.0.0.0/0
```

### Architecture Diagram (Text Format)

```
┌─────────────────────────────────────────────────┐
│              AWS Region (us-east-1)             │
├─────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────┐ │
│  │           VPC (10.0.0.0/16)                │ │
│  │  ┌──────────────┐    ┌──────────────┐     │ │
│  │  │ Subnet AZ-1  │    │ Subnet AZ-2  │     │ │
│  │  │              │    │              │     │ │
│  │  │ ┌──────────┐ │    │ ┌──────────┐ │     │ │
│  │  │ │ EC2      │ │    │ │ EC2      │ │     │ │
│  │  │ │ Instance │ │    │ │ Instance │ │     │ │
│  │  │ └──────────┘ │    │ └──────────┘ │     │ │
│  │  └──────────────┘    └──────────────┘     │ │
│  └────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
         │
         │ Security Group (Firewall)
         └─ Allow SSH (22), HTTP (80), HTTPS (443)
```

### Common Mistakes Beginners Make

1. **Leaving SSH port 22 open to 0.0.0.0/0**: Restrict to specific IPs or VPN
2. **Not using key pairs properly**: Store keys securely, never share them
3. **Running expensive instances when not needed**: Stop instances to save money
4. **Ignoring security group rules**: Be explicit about inbound/outbound rules
5. **Not using Auto Scaling**: Manual scaling leads to downtime and costs
6. **Using default VPC for production**: Create custom VPCs for better isolation

### Interview Questions

1. **What is the difference between stopping and terminating an EC2 instance?**
   - Stopped: Instance can be restarted, data persists on EBS
   - Terminated: Instance is deleted, EBS data lost (unless backed up)

2. **Explain the different instance types and when to use them.**
   - t2/t3: Dev/test environments
   - m5/m6: Web applications, small databases
   - c5/c6: Data processing, high CPU needs
   - r5/r6: In-memory databases, caching

3. **What is an AMI and why is it useful?**
   - Template containing OS and software
   - Useful for quickly launching identical instances
   - Can be shared across regions and accounts

4. **How do security groups differ from NACLs?**
   - Security groups: Stateful, instance-level, allows/denies rules
   - NACLs: Stateless, subnet-level, allows/denies rules

5. **How would you monitor EC2 instance health?**
   - Use CloudWatch metrics (CPU, network)
   - Set up alarms for threshold violations
   - Use Auto Scaling health checks

### Mini Project: Multi-Tier Web Application

**Objective**: Deploy a 2-tier web application with EC2

**Requirements**:
- Web tier: Apache server on EC2
- Database tier: RDS MySQL instance
- Security groups: Restrict database access to web servers only
- Key pairs: Secure SSH access

**Steps**:
1. Create security groups for web and database tiers
2. Launch EC2 instance for web server
3. Install Apache and PHP
4. Create RDS database instance
5. Configure web server to connect to database
6. Test application connectivity

---

## 2. Amazon S3 (Simple Storage Service)

### What is S3?
S3 is AWS's object storage service that stores data as objects within buckets. Unlike traditional file systems, S3 stores unlimited objects with built-in redundancy across multiple data centers.

### Why Use S3?
**Real-World Example**: Airbnb uses S3 to store millions of property photos. Users can upload images, and Airbnb serves them globally with CloudFront, ensuring fast delivery worldwide.

**Advantages**:
- Unlimited storage capacity
- 99.999999999% (11 nines) durability
- Global distribution capabilities
- Cost-effective for infrequent access
- Built-in versioning and backup

### Key Concepts

**Bucket Structure**:
```
Bucket: my-company-data
├── photos/
│   ├── profile1.jpg
│   ├── profile2.jpg
├── documents/
│   ├── report.pdf
└── backups/
    ├── db-backup-2024.tar.gz
```

**Storage Classes**:
- S3 Standard: Frequent access, 99.99% availability
- S3 Standard-IA: Infrequent access, lower cost
- S3 Glacier: Archive data, very low cost
- S3 Glacier Deep Archive: Long-term archival

**Object Metadata**:
- Content-Type: Type of object (image/png, application/pdf)
- Cache-Control: Browser caching rules
- Metadata Tags: Custom key-value pairs
- Server-Side Encryption: Encryption method

### Step-by-Step Setup Guide

#### Step 1: Create an S3 Bucket
```bash
# Create bucket (globally unique name)
aws s3 mb s3://my-unique-bucket-name

# Create bucket in specific region
aws s3 mb s3://my-bucket --region us-west-2
```

#### Step 2: Upload Objects
```bash
# Upload single file
aws s3 cp document.pdf s3://my-bucket/documents/

# Upload entire directory
aws s3 cp ./photos s3://my-bucket/photos --recursive

# Upload with metadata
aws s3 cp image.jpg s3://my-bucket/images/ \
  --metadata "project=marketing,author=john"
```

#### Step 3: Configure Versioning
```bash
# Enable versioning
aws s3api put-bucket-versioning \
  --bucket my-bucket \
  --versioning-configuration Status=Enabled

# List all versions of object
aws s3api list-object-versions --bucket my-bucket
```

#### Step 4: Set Bucket Policy
```bash
# Create policy file (bucket-policy.json)
cat > bucket-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-123456"
        }
      }
    }
  ]
}
EOF

# Apply policy
aws s3api put-bucket-policy --bucket my-bucket --policy file://bucket-policy.json
```

#### Step 5: Configure Lifecycle Rules
```bash
# Create lifecycle policy (lifecycle.json)
cat > lifecycle.json << 'EOF'
{
  "Rules": [
    {
      "ID": "Archive old objects",
      "Filter": {"Prefix": "logs/"},
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "GLACIER"
        }
      ],
      "Expiration": {
        "Days": 365
      }
    }
  ]
}
EOF

# Apply lifecycle policy
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-bucket \
  --lifecycle-configuration file://lifecycle.json
```

### Important Commands

```bash
# List all buckets
aws s3 ls

# List objects in bucket
aws s3 ls s3://my-bucket/

# Copy between buckets
aws s3 cp s3://source-bucket/file.txt s3://dest-bucket/

# Delete object
aws s3 rm s3://my-bucket/file.txt

# Delete bucket (must be empty)
aws s3 rb s3://my-bucket

# Sync buckets (S3 sync)
aws s3 sync s3://source-bucket s3://dest-bucket

# Enable encryption
aws s3api put-bucket-encryption \
  --bucket my-bucket \
  --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'

# Block public access
aws s3api put-public-access-block \
  --bucket my-bucket \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

### Architecture Diagram

```
┌─────────────────────────────────────┐
│      S3 Bucket: my-bucket           │
├─────────────────────────────────────┤
│                                     │
│  Objects organized by prefix:       │
│  ├── documents/                     │
│  │   ├── report.pdf                 │
│  │   └── presentation.pptx          │
│  ├── images/                        │
│  │   ├── photo1.jpg                 │
│  │   └── photo2.jpg                 │
│  └── archives/                      │
│      └── backup-2024.tar.gz         │
│                                     │
│  Features:                          │
│  ✓ Versioning enabled               │
│  ✓ Lifecycle policies               │
│  ✓ Server-side encryption           │
│  ✓ Access logging                   │
└─────────────────────────────────────┘
         │
         │ CloudFront (CDN)
         │ Global edge locations
         └─→ Users worldwide
```

### Common Mistakes Beginners Make

1. **Making buckets publicly readable by accident**: Always use bucket policies carefully
2. **Not enabling versioning before disaster**: Enable versioning from day one
3. **Storing sensitive data unencrypted**: Always encrypt sensitive data
4. **Not using lifecycle policies**: Paying for data that could be archived
5. **Incorrect bucket naming**: Bucket names must be globally unique and lowercase
6. **Not backing up important data**: Use cross-region replication

### Interview Questions

1. **What is the maximum size of an object in S3?**
   - 5TB via multipart upload (single PUT limited to 5GB)

2. **How does S3 achieve 11 nines of durability?**
   - Replicates objects across multiple facilities
   - Uses checksums to detect corruption
   - Automatically replaces corrupted copies

3. **What's the difference between S3 Standard and S3 Glacier?**
   - Standard: Instant access, higher cost
   - Glacier: 1-5 minutes retrieval, lower cost, for archival

4. **How would you secure sensitive data in S3?**
   - Enable bucket encryption (SSE-S3 or SSE-KMS)
   - Block public access
   - Enable MFA delete protection
   - Use bucket policies and IAM roles

5. **Explain S3 versioning and why it's important.**
   - Keeps all versions of an object
   - Protects against accidental deletion
   - Allows rollback to previous versions

### Mini Project: Static Website Hosting

**Objective**: Host a static website on S3 with CloudFront

**Requirements**:
- Create S3 bucket for website files
- Configure static website hosting
- Set up CloudFront distribution for caching
- Enable HTTPS
- Add custom domain (optional)

**Steps**:
1. Create S3 bucket
2. Upload HTML, CSS, JS files
3. Enable static website hosting
4. Create CloudFront distribution
5. Point domain to CloudFront
6. Test website accessibility

---

## 3. AWS IAM (Identity and Access Management)

### What is IAM?
IAM is AWS's centralized access control service that manages who can do what within your AWS account. It allows you to create users, roles, policies, and control fine-grained permissions across all AWS services.

### Why Use IAM?
**Real-World Example**: A startup has developers, DevOps engineers, and finance teams. IAM allows:
- Developers: EC2, S3, CloudWatch access only
- DevOps: Full access to deployment services
- Finance: Billing and cost management access only
- Root account: Never used, kept secure

**Advantages**:
- Granular access control
- Multi-factor authentication (MFA)
- Temporary security credentials
- Cross-account access
- Service roles for applications

### Key Concepts

**IAM Components**:
```
IAM User: Individual person or application
  ├── Access Keys: Long-term credentials (like username/password)
  └── MFA Device: Hardware or virtual MFA authenticator

IAM Role: Temporary credentials for services
  ├── Trust Policy: Who can assume the role
  └── Permissions: What actions they can perform

IAM Policy: JSON document defining permissions
  ├── Effect: Allow or Deny
  ├── Action: Specific API actions
  ├── Resource: AWS resources (ARN format)
  └── Condition: Optional conditions (IP, time, etc.)

IAM Group: Collection of users with same permissions
```

**Principal of Least Privilege**:
- Grant minimum permissions needed
- Regularly audit and remove unused permissions
- Use resource-level permissions when possible

**ARN Format** (Amazon Resource Name):
```
arn:aws:service:region:account-id:resource-type/resource-id
arn:aws:s3:::my-bucket
arn:aws:ec2:us-east-1:123456789012:instance/i-1234567
arn:aws:iam::123456789012:user/john
```

### Step-by-Step Setup Guide

#### Step 1: Create IAM User
```bash
# Create user
aws iam create-user --user-name john-dev

# Create another user
aws iam create-user --user-name jane-devops

# List users
aws iam list-users
```

#### Step 2: Create Access Keys
```bash
# Create access keys for user
aws iam create-access-key --user-name john-dev

# Output format:
# {
#   "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
#   "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
# }

# Store safely - not shown again!
```

#### Step 3: Create IAM Groups
```bash
# Create developer group
aws iam create-group --group-name developers

# Create devops group
aws iam create-group --group-name devops

# Add user to group
aws iam add-user-to-group --group-name developers --user-name john-dev
```

#### Step 4: Create Custom Policy
```bash
# Create policy file (dev-policy.json)
cat > dev-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::dev-bucket",
        "arn:aws:s3:::dev-bucket/*"
      ]
    },
    {
      "Effect": "Deny",
      "Action": "iam:*",
      "Resource": "*"
    }
  ]
}
EOF

# Create policy
aws iam create-policy \
  --policy-name dev-policy \
  --policy-document file://dev-policy.json

# Attach to group
aws iam attach-group-policy \
  --group-name developers \
  --policy-arn arn:aws:iam::123456789012:policy/dev-policy
```

#### Step 5: Enable MFA
```bash
# Create virtual MFA device
aws iam enable-mfa-device \
  --user-name john-dev \
  --serial-number arn:aws:iam::123456789012:mfa/john-device \
  --authentication-code1 123456 \
  --authentication-code2 654321

# Alternatively, use Google Authenticator or Authy
```

#### Step 6: Create IAM Role for Service
```bash
# Create trust policy (trust-policy.json)
cat > trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

# Create role
aws iam create-role \
  --role-name ec2-app-role \
  --assume-role-policy-document file://trust-policy.json

# Create instance profile
aws iam create-instance-profile --instance-profile-name ec2-app-profile

# Add role to instance profile
aws iam add-role-to-instance-profile \
  --instance-profile-name ec2-app-profile \
  --role-name ec2-app-role

# Attach policy to role
aws iam attach-role-policy \
  --role-name ec2-app-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

### Important Commands

```bash
# List IAM users
aws iam list-users

# Get user details
aws iam get-user --user-name john-dev

# List user groups
aws iam list-groups-for-user --user-name john-dev

# List user policies
aws iam list-user-policies --user-name john-dev

# Create access key
aws iam create-access-key --user-name john-dev

# Delete access key
aws iam delete-access-key --user-name john-dev --access-key-id AKIAIOSFODNN7EXAMPLE

# List IAM roles
aws iam list-roles

# Get current caller identity
aws sts get-caller-identity

# Assume role (generate temporary credentials)
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/MyRole \
  --role-session-name my-session

# List all policies
aws iam list-policies

# View policy details
aws iam get-policy-version \
  --policy-arn arn:aws:iam::123456789012:policy/dev-policy \
  --version-id v1
```

### Architecture Diagram

```
┌──────────────────────────────────────────────────┐
│           AWS Account (123456789012)             │
├──────────────────────────────────────────────────┤
│                                                  │
│  ┌─────────────────────────────────────────┐   │
│  │     IAM Users & Groups                  │   │
│  │  ┌──────────────────────────────────┐   │   │
│  │  │ Developers Group                 │   │   │
│  │  │ ├─ john-dev                      │   │   │
│  │  │ ├─ jane-dev                      │   │   │
│  │  │ └─ Policy: dev-policy            │   │   │
│  │  └──────────────────────────────────┘   │   │
│  │  ┌──────────────────────────────────┐   │   │
│  │  │ DevOps Group                     │   │   │
│  │  │ ├─ alice-devops                  │   │   │
│  │  │ └─ Policy: admin-policy          │   │   │
│  │  └──────────────────────────────────┘   │   │
│  └─────────────────────────────────────────┘   │
│                                                  │
│  ┌─────────────────────────────────────────┐   │
│  │     IAM Roles (for Services)            │   │
│  │  ┌──────────────────────────────────┐   │   │
│  │  │ EC2-App-Role                     │   │   │
│  │  │ ├─ Assumable by: EC2 Service     │   │   │
│  │  │ └─ Policy: S3ReadOnly            │   │   │
│  │  └──────────────────────────────────┘   │   │
│  │  ┌──────────────────────────────────┐   │   │
│  │  │ Lambda-Execution-Role            │   │   │
│  │  │ ├─ Assumable by: Lambda Service  │   │   │
│  │  │ └─ Policy: CloudWatch+S3         │   │   │
│  │  └──────────────────────────────────┘   │   │
│  └─────────────────────────────────────────┘   │
│                                                  │
│  ┌─────────────────────────────────────────┐   │
│  │  AWS Services (using roles)             │   │
│  │  ├─ EC2 Instance (assumes EC2-Role)     │   │
│  │  ├─ Lambda Function (assumes Lambda-Role)   │
│  │  └─ RDS Instance (uses IAM auth)        │   │
│  └─────────────────────────────────────────┘   │
│                                                  │
└──────────────────────────────────────────────────┘
```

### Common Mistakes Beginners Make

1. **Using root account for daily work**: Create IAM users for everyone
2. **Sharing access keys**: Each user should have unique keys
3. **Not using MFA**: Always enable MFA for sensitive accounts
4. **Over-permissive policies**: Grant only necessary permissions
5. **Not rotating access keys**: Rotate keys every 90 days
6. **Using long-term credentials in applications**: Use roles instead
7. **Not auditing IAM**: Regularly review who has access

### Interview Questions

1. **What is the difference between IAM Users and Roles?**
   - Users: Long-term identity with access keys
   - Roles: Temporary credentials, assumed by services or users

2. **Explain the Principal of Least Privilege.**
   - Grant minimum permissions needed for a task
   - Regularly audit and remove unnecessary permissions
   - Reduces security risk if credentials are compromised

3. **How do you implement cross-account access?**
   - Create role in target account with trust policy
   - Trust policy specifies source account ARN
   - User in source account assumes role in target account

4. **What's the difference between a Policy and a Role?**
   - Policy: Document defining permissions
   - Role: Identity with assumed policies and trust relationships

5. **How would you securely share AWS resources with contractors?**
   - Create temporary IAM role
   - Set assume-role permissions with time limits
   - Use external ID for additional security
   - Monitor access via CloudTrail

### Mini Project: Multi-Environment Access Control

**Objective**: Set up IAM structure for dev, staging, and production

**Requirements**:
- Create separate IAM users for different teams
- Create groups with appropriate permissions
- Implement dev, staging, and prod environment access
- Enable MFA for production access
- Create service roles for EC2 and Lambda

**Steps**:
1. Create IAM users for developers, DevOps, and admins
2. Create groups (dev-team, devops-team, admins)
3. Create environment-specific policies
4. Create roles for EC2 and Lambda services
5. Configure MFA for sensitive operations
6. Document access matrix

---

## 4. Amazon VPC (Virtual Private Cloud)

### What is VPC?
A VPC is a logically isolated network environment within AWS where you can launch AWS resources. It gives you complete control over your network, including IP address ranges, subnets, route tables, and gateways.

### Why Use VPC?
**Real-World Example**: A healthcare company requires HIPAA compliance and network isolation. Using VPC, they create:
- Private subnet for databases (no internet access)
- Private subnet for application servers
- Bastion host in public subnet for secure access
- Network ACLs restricting traffic between subnets

**Advantages**:
- Complete network control
- Enhanced security with private subnets
- Multi-layer security with NACLs and Security Groups
- Support for hybrid cloud (VPN, Direct Connect)
- Scalable network architecture

### Key Concepts

**VPC Components**:
```
VPC: 10.0.0.0/16 (Virtual network)
├── Subnet AZ-1: 10.0.1.0/24 (Public subnet)
│   └── Route Table: Internet Gateway route
├── Subnet AZ-2: 10.0.2.0/24 (Public subnet)
│   └── Route Table: Internet Gateway route
├── Subnet AZ-1: 10.0.11.0/24 (Private subnet)
│   └── Route Table: NAT Gateway route
└── Subnet AZ-2: 10.0.12.0/24 (Private subnet)
    └── Route Table: NAT Gateway route

Internet Gateway: Allows internet communication
NAT Gateway: Allows private instances to reach internet
VPN Gateway: Connects to on-premises networks
```

**CIDR Notation**:
- `10.0.0.0/16` = Network with 65,536 addresses (10.0.0.0 to 10.0.255.255)
- `10.0.1.0/24` = Subnet with 256 addresses (10.0.1.0 to 10.0.1.255)
- `/8` = Class A, `/16` = Class B, `/24` = Class C

**Route Table**:
- Controls how packets are routed
- Destination CIDR + Target (IGW, NAT, VPN, etc.)

### Step-by-Step Setup Guide

#### Step 1: Create VPC
```bash
# Create VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16

# Enable DNS resolution (important!)
aws ec2 modify-vpc-attribute \
  --vpc-id vpc-xxxxxxxx \
  --enable-dns-resolution

aws ec2 modify-vpc-attribute \
  --vpc-id vpc-xxxxxxxx \
  --enable-dns-hostnames
```

#### Step 2: Create Internet Gateway
```bash
# Create Internet Gateway
aws ec2 create-internet-gateway

# Attach to VPC
aws ec2 attach-internet-gateway \
  --internet-gateway-id igw-xxxxxxxx \
  --vpc-id vpc-xxxxxxxx
```

#### Step 3: Create Subnets
```bash
# Create public subnet AZ-1
aws ec2 create-subnet \
  --vpc-id vpc-xxxxxxxx \
  --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a

# Create public subnet AZ-2
aws ec2 create-subnet \
  --vpc-id vpc-xxxxxxxx \
  --cidr-block 10.0.2.0/24 \
  --availability-zone us-east-1b

# Create private subnet AZ-1
aws ec2 create-subnet \
  --vpc-id vpc-xxxxxxxx \
  --cidr-block 10.0.11.0/24 \
  --availability-zone us-east-1a

# Create private subnet AZ-2
aws ec2 create-subnet \
  --vpc-id vpc-xxxxxxxx \
  --cidr-block 10.0.12.0/24 \
  --availability-zone us-east-1b
```

#### Step 4: Create Route Tables
```bash
# Create route table for public subnets
aws ec2 create-route-table --vpc-id vpc-xxxxxxxx

# Add route to Internet Gateway
aws ec2 create-route \
  --route-table-id rtb-xxxxxxxx \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id igw-xxxxxxxx

# Associate subnets with route table
aws ec2 associate-route-table \
  --route-table-id rtb-xxxxxxxx \
  --subnet-id subnet-xxxxxxxx (public subnet 1)

aws ec2 associate-route-table \
  --route-table-id rtb-xxxxxxxx \
  --subnet-id subnet-xxxxxxxx (public subnet 2)
```

#### Step 5: Create NAT Gateway (for private subnets)
```bash
# Allocate Elastic IP
aws ec2 allocate-address --domain vpc

# Create NAT Gateway in public subnet
aws ec2 create-nat-gateway \
  --subnet-id subnet-xxxxxxxx \
  --allocation-id eipalloc-xxxxxxxx

# Create route table for private subnets
aws ec2 create-route-table --vpc-id vpc-xxxxxxxx

# Add route to NAT Gateway
aws ec2 create-route \
  --route-table-id rtb-private \
  --destination-cidr-block 0.0.0.0/0 \
  --nat-gateway-id nat-xxxxxxxx

# Associate private subnets
aws ec2 associate-route-table \
  --route-table-id rtb-private \
  --subnet-id subnet-private1

aws ec2 associate-route-table \
  --route-table-id rtb-private \
  --subnet-id subnet-private2
```

#### Step 6: Create Network ACLs (Optional)
```bash
# Create NACL
aws ec2 create-network-acl --vpc-id vpc-xxxxxxxx

# Add inbound rule (allow HTTP)
aws ec2 create-network-acl-entry \
  --network-acl-id acl-xxxxxxxx \
  --rule-number 100 \
  --protocol tcp \
  --port-range FromPort=80,ToPort=80 \
  --cidr-block 0.0.0.0/0 \
  --ingress

# Associate with subnet
aws ec2 associate-network-acl-with-subnet \
  --network-acl-id acl-xxxxxxxx \
  --subnet-id subnet-xxxxxxxx
```

### Important Commands

```bash
# List VPCs
aws ec2 describe-vpcs

# List subnets
aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-xxxxxxxx"

# List route tables
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-xxxxxxxx"

# List Internet Gateways
aws ec2 describe-internet-gateways

# List NAT Gateways
aws ec2 describe-nat-gateways

# Create VPN Connection
aws ec2 create-vpn-connection \
  --type ipsec.1 \
  --customer-gateway-id cgw-xxxxxxxx \
  --vpn-gateway-id vgw-xxxxxxxx

# List security groups
aws ec2 describe-security-groups --filters "Name=vpc-id,Values=vpc-xxxxxxxx"

# Delete VPC (must delete all resources first)
aws ec2 delete-vpc --vpc-id vpc-xxxxxxxx
```

### Architecture Diagram

```
┌────────────────────────────────────────────────────────┐
│              AWS Region: us-east-1                     │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌──────────────────────────────────────────────────┐ │
│  │     VPC: 10.0.0.0/16                            │ │
│  │                                                  │ │
│  │  Internet Gateway (IGW)                         │ │
│  │           ↓                                      │ │
│  │  ┌────────────────────────────────────────┐     │ │
│  │  │    Public Subnets (with NAT Gateway)  │     │ │
│  │  │                                        │     │ │
│  │  │  AZ-1: 10.0.1.0/24      AZ-2: 10.0.2.0/24  │ │
│  │  │  ┌──────────────────┐   ┌──────────────┐   │ │
│  │  │  │ EC2 Web Server   │   │ EC2 Web Srv  │   │ │
│  │  │  │ 10.0.1.10        │   │ 10.0.2.10    │   │ │
│  │  │  └──────────────────┘   └──────────────┘   │ │
│  │  └────────────────────────────────────────┘   │ │
│  │            ↓  (Route to 0.0.0.0/0 → IGW)      │ │
│  │                                                │ │
│  │  ┌────────────────────────────────────────┐   │ │
│  │  │   Private Subnets (App Layer)         │   │ │
│  │  │                                        │   │ │
│  │  │  AZ-1: 10.0.11.0/24  AZ-2: 10.0.12.0/24 │ │
│  │  │  ┌──────────────────┐  ┌──────────────┐ │ │
│  │  │  │ EC2 App Server   │  │ EC2 App Srv  │ │ │
│  │  │  │ 10.0.11.10       │  │ 10.0.12.10   │ │ │
│  │  │  └──────────────────┘  └──────────────┘ │ │
│  │  └────────────────────────────────────────┘ │ │
│  │            ↓  (Route to 0.0.0.0/0 → NAT)    │ │
│  │                                              │ │
│  │  ┌────────────────────────────────────────┐ │ │
│  │  │   Private Subnets (Database Layer)    │ │ │
│  │  │                                        │ │ │
│  │  │  AZ-1: 10.0.21.0/24  AZ-2: 10.0.22.0/24 │ │
│  │  │  ┌──────────────────┐  ┌──────────────┐ │ │
│  │  │  │ RDS Primary      │  │ RDS Standby  │ │ │
│  │  │  │ 10.0.21.10       │  │ 10.0.22.10   │ │ │
│  │  │  └──────────────────┘  └──────────────┘ │ │
│  │  └────────────────────────────────────────┘ │ │
│  │         ↓ (No internet route)                 │ │
│  │                                              │ │
│  └──────────────────────────────────────────────┘ │
│                                                    │
│  NAT Gateway (in public subnet for outbound)     │
│          ↓                                         │
│  Elastic IP: 203.0.113.10                        │
│                                                    │
└────────────────────────────────────────────────────┘
         ↓
   Internet (0.0.0.0/0)
```

### Common Mistakes Beginners Make

1. **Not planning IP ranges properly**: Use CIDR calculator tool
2. **Putting sensitive resources in public subnets**: Always use private subnets for databases
3. **Forgetting NAT Gateway costs**: NAT Gateway is expensive, plan accordingly
4. **Incorrect route table associations**: Double-check subnet routes
5. **Not enabling DNS resolution**: Can't resolve names without it
6. **Using default VPC for production**: Create custom VPCs for better isolation
7. **Not documenting network architecture**: Maintain network diagrams

### Interview Questions

1. **What's the difference between Public and Private subnets?**
   - Public: Route to Internet Gateway, instances get public IPs
   - Private: Route to NAT Gateway, instances don't get public IPs

2. **How do you make a private instance access the internet?**
   - Place NAT Gateway in public subnet
   - Route private traffic to NAT Gateway
   - NAT translates private IPs to Elastic IP

3. **What's the difference between Security Groups and NACLs?**
   - Security Groups: Stateful, instance-level, whitelist only
   - NACLs: Stateless, subnet-level, allow and deny rules

4. **How would you implement a bastion host?**
   - Launch EC2 in public subnet
   - Security group allows SSH from trusted IPs
   - SSH to bastion, then to private instances
   - Useful for secure access to private resources

5. **Explain VPC Peering and when to use it.**
   - Allows communication between VPCs as if on same network
   - Use for: Multi-account architectures, third-party integrations
   - No data transfer charges within same region

### Mini Project: Three-Tier Architecture

**Objective**: Design and implement a secure three-tier VPC architecture

**Requirements**:
- Public subnet: Web servers with load balancer
- Private app subnet: Application servers
- Private database subnet: RDS database
- NAT Gateway for outbound traffic
- Security groups restricting layer-to-layer communication

**Steps**:
1. Create VPC with CIDR block 10.0.0.0/16
2. Create public subnets in 2 AZs
3. Create private app subnets in 2 AZs
4. Create private database subnets in 2 AZs
5. Configure route tables for each tier
6. Create security groups:
   - Web: Allow HTTP/HTTPS from internet
   - App: Allow requests from web tier only
   - Database: Allow MySQL from app tier only
7. Launch instances in each tier
8. Test connectivity between tiers

---

## 5. Amazon RDS (Relational Database Service)

### What is RDS?
RDS is AWS's managed relational database service that handles database administration tasks like backups, patching, and replication. Supported engines: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server.

### Why Use RDS?
**Real-World Example**: Spotify uses RDS to manage their massive user database. Instead of managing servers, Spotify focuses on their application while AWS handles:
- Daily automated backups
- Multi-AZ replication for high availability
- Automatic failover in case of failure
- Read replicas for scaling read performance

**Advantages**:
- Automated backups and patches
- Multi-AZ for high availability
- Read replicas for scaling
- Managed security (encryption, VPC support)
- Automated minor version upgrades
- Performance insights

### Key Concepts

**RDS Components**:
```
RDS Instance (Primary)
├── Automated Backups (35 days retention)
├── Multi-AZ Standby (synchronous replication)
└── Read Replicas (asynchronous replication)
    ├── In same region
    ├── In different regions
    └── Can be promoted to standalone
```

**Database Engines**:
- MySQL: Open source, fast, reliable
- PostgreSQL: Advanced features, ACID compliance
- MariaDB: MySQL compatible, open source
- Oracle: Enterprise database, expensive
- SQL Server: Microsoft database, Windows compatible

**Backup Strategy**:
- Automated: Daily snapshots (configurable retention)
- Manual: On-demand snapshots
- Retention: 1-35 days for automated backups

### Step-by-Step Setup Guide

#### Step 1: Create DB Subnet Group
```bash
# Create subnet group (required for RDS)
aws rds create-db-subnet-group \
  --db-subnet-group-name my-db-subnet-group \
  --db-subnet-group-description "Subnet group for RDS" \
  --subnet-ids subnet-xxxxxxxx subnet-yyyyyyyy

# List subnet groups
aws rds describe-db-subnet-groups
```

#### Step 2: Create Security Group for RDS
```bash
# Create security group for RDS
aws ec2 create-security-group \
  --group-name rds-sg \
  --description "Security group for RDS MySQL" \
  --vpc-id vpc-xxxxxxxx

# Allow MySQL traffic from application servers
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxxxxx \
  --protocol tcp \
  --port 3306 \
  --source-group sg-app-servers
```

#### Step 3: Create RDS Instance
```bash
# Create RDS instance
aws rds create-db-instance \
  --db-instance-identifier my-app-db \
  --db-instance-class db.t3.micro \
  --engine mysql \
  --engine-version 8.0.28 \
  --master-username admin \
  --master-user-password MySecurePassword123! \
  --allocated-storage 20 \
  --storage-type gp2 \
  --db-subnet-group-name my-db-subnet-group \
  --vpc-security-group-ids sg-xxxxxxxx \
  --backup-retention-period 7 \
  --multi-az \
  --enable-cloudwatch-logs-exports error general slowquery

# Note: Store password securely, not in scripts!
```

#### Step 4: Configure Enhanced Monitoring
```bash
# Create IAM role for enhanced monitoring
aws iam create-role \
  --role-name rds-monitoring-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "monitoring.rds.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Attach policy
aws iam attach-role-policy \
  --role-name rds-monitoring-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole

# Modify DB instance to enable monitoring
aws rds modify-db-instance \
  --db-instance-identifier my-app-db \
  --enable-iam-database-authentication \
  --monitoring-interval 60 \
  --monitoring-role-arn arn:aws:iam::123456789012:role/rds-monitoring-role \
  --apply-immediately
```

#### Step 5: Create Read Replica
```bash
# Create read replica (for scaling read operations)
aws rds create-db-instance-read-replica \
  --db-instance-identifier my-app-db-read-replica \
  --source-db-instance-identifier my-app-db

# Create cross-region read replica
aws rds create-db-instance-read-replica \
  --db-instance-identifier my-app-db-read-replica-us-west-2 \
  --source-db-instance-identifier my-app-db \
  --region us-west-2
```

#### Step 6: Backup and Restore
```bash
# Create manual snapshot
aws rds create-db-snapshot \
  --db-snapshot-identifier my-db-snapshot-2024 \
  --db-instance-identifier my-app-db

# List snapshots
aws rds describe-db-snapshots

# Restore from snapshot
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier my-app-db-restored \
  --db-snapshot-identifier my-db-snapshot-2024

# Restore to point in time
aws rds restore-db-instance-to-point-in-time \
  --source-db-instance-identifier my-app-db \
  --target-db-instance-identifier my-app-db-restored \
  --restore-time 2024-01-15T10:00:00Z
```

### Important Commands

```bash
# Describe RDS instance
aws rds describe-db-instances --db-instance-identifier my-app-db

# Modify RDS instance
aws rds modify-db-instance \
  --db-instance-identifier my-app-db \
  --allocated-storage 100 \
  --apply-immediately

# Reboot RDS instance
aws rds reboot-db-instance --db-instance-identifier my-app-db

# Enable automated backups
aws rds modify-db-instance \
  --db-instance-identifier my-app-db \
  --backup-retention-period 30

# Delete RDS instance
aws rds delete-db-instance \
  --db-instance-identifier my-app-db \
  --skip-final-snapshot

# List events
aws rds describe-events --source-type db-instance

# Create option group
aws rds create-option-group \
  --option-group-name myoptiongroup \
  --engine-name mysql \
  --major-engine-version 8.0 \
  --option-group-description "My option group"
```

### Architecture Diagram

```
┌──────────────────────────────────────────────────────┐
│            RDS Multi-AZ Architecture                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│  ┌─────────────────────────────────────────────┐   │
│  │    Application Layer (Multiple EC2s)       │   │
│  └──────────────────┬──────────────────────────┘   │
│                     │                               │
│                     │ (Application connects here)   │
│                     ↓                               │
│  ┌─────────────────────────────────────────────┐   │
│  │    RDS Primary Instance (AZ-1)             │   │
│  │    - Accepts reads and writes              │   │
│  │    - Automatic backup every 5 minutes      │   │
│  │    - 20GB storage (gp2)                    │   │
│  └────────────────┬────────────────────────────┘   │
│                   │                                 │
│        Synchronous Replication (same AZ)           │
│                   ↓                                 │
│  ┌─────────────────────────────────────────────┐   │
│  │    RDS Standby Instance (AZ-2)             │   │
│  │    - Hot standby, can't connect             │   │
│  │    - Automatic failover in case of failure  │   │
│  │    - Same specs as primary                 │   │
│  └─────────────────────────────────────────────┘   │
│                                                      │
│  Backup Locations:                                  │
│  ├─ Daily snapshots (up to 35 days)               │
│  ├─ Transaction logs (point-in-time recovery)     │
│  └─ Automated backup retention: 7 days            │
│                                                      │
│  Optional Read Replicas (for scaling reads):       │
│  ├─ Same region read replica (low latency)        │
│  ├─ Cross-region read replica (disaster recovery) │
│  └─ Can be promoted to standalone instance        │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Common Mistakes Beginners Make

1. **Not enabling Multi-AZ for production**: Always use Multi-AZ for availability
2. **Storing database passwords in code**: Use Secrets Manager or Parameter Store
3. **Not backing up data**: Set backup retention to at least 7 days
4. **Using public accessibility**: Keep databases in private subnets
5. **Not monitoring database performance**: Set up CloudWatch alarms
6. **Underestimating storage needs**: Start with more than you think needed
7. **Not testing restore procedures**: Regularly test backup restoration

### Interview Questions

1. **What is Multi-AZ and how does it improve availability?**
   - Synchronously replicates data to standby in different AZ
   - Automatic failover if primary fails (typically < 2 minutes)
   - Zero data loss with synchronous replication

2. **Explain the difference between Multi-AZ and Read Replicas.**
   - Multi-AZ: For high availability, automatic failover
   - Read Replicas: For scaling reads, manual failover, async replication

3. **How would you back up an RDS database?**
   - Automated backups: AWS manages, retention up to 35 days
   - Manual snapshots: On-demand, retained indefinitely
   - Backup locations: S3 (managed by AWS)

4. **What's the best way to handle database scaling?**
   - Vertical: Increase instance size (simple, causes downtime)
   - Horizontal: Read replicas (better for read-heavy workloads)
   - Database optimization: Query tuning, indexing

5. **How do you ensure database security in AWS?**
   - Use VPC security groups (restrict network access)
   - Enable encryption at rest (KMS) and in transit (SSL/TLS)
   - Use IAM database authentication
   - Regular backups and monitoring

### Mini Project: Highly Available Database Setup

**Objective**: Create a highly available RDS setup with read replicas

**Requirements**:
- Multi-AZ RDS instance for primary database
- Read replica in same region for read scaling
- Cross-region read replica for disaster recovery
- Automated backups with 30-day retention
- CloudWatch monitoring and alarms
- Parameter Store for database credentials

**Steps**:
1. Create DB subnet group in private subnets
2. Create security group allowing traffic from app tier
3. Launch Multi-AZ RDS MySQL instance
4. Store master password in Secrets Manager
5. Create same-region read replica
6. Create cross-region read replica
7. Set up CloudWatch monitoring:
   - CPU utilization alarm
   - Database connections alarm
   - Replication lag alarm
8. Test failover and restore procedures

---

## 6. Elastic Load Balancing (ELB)

### What is ELB?
ELB automatically distributes incoming application traffic across multiple targets (EC2 instances, containers, IP addresses) to ensure no single instance becomes a bottleneck. Three types: Application Load Balancer (ALB), Network Load Balancer (NLB), Classic Load Balancer (deprecated).

### Why Use ELB?
**Real-World Example**: An e-commerce platform during Black Friday receives 100x normal traffic. With ELB:
- Traffic is distributed across 100 EC2 instances
- User requests are routed to healthy instances only
- Failed instances are automatically removed from the pool
- New instances are automatically added to handle spikes

**Advantages**:
- High availability and fault tolerance
- Automatic scaling integration
- Health checks for removing unhealthy targets
- Session persistence (sticky sessions)
- HTTPS/SSL termination
- Multiple availability zones support

### Key Concepts

**Load Balancer Types**:

**Application Load Balancer (ALB)**:
- Layer 7 (Application) routing
- Best for: Web apps, APIs, microservices
- Features: Host-based routing, path-based routing, HTTP/HTTPS

**Network Load Balancer (NLB)**:
- Layer 4 (Transport) routing
- Best for: Extreme performance, non-HTTP protocols
- Features: Ultra-high performance, TCP/UDP, millions of requests/sec

**Classic Load Balancer (CLB)**:
- Deprecated, don't use for new applications
- Layer 4 and 7 (both)

**Health Checks**:
```
Target Health Check Process:
1. Load balancer sends HTTP request to target
2. Target responds with HTTP status code
3. 200-399: Healthy
4. 400+: Unhealthy
5. No response: Unhealthy
6. After X consecutive unhealthy checks → removed from pool
```

### Step-by-Step Setup Guide

#### Step 1: Create Target Group
```bash
# Create target group for ALB
aws elbv2 create-target-group \
  --name my-targets \
  --protocol HTTP \
  --port 80 \
  --vpc-id vpc-xxxxxxxx

# Configure health check
aws elbv2 modify-target-group \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890abcdef \
  --health-check-protocol HTTP \
  --health-check-path /health \
  --health-check-interval-seconds 30 \
  --health-check-timeout-seconds 5 \
  --healthy-threshold-count 2 \
  --unhealthy-threshold-count 2
```

#### Step 2: Create Application Load Balancer
```bash
# Create load balancer
aws elbv2 create-load-balancer \
  --name my-alb \
  --subnets subnet-12345678 subnet-87654321 \
  --security-groups sg-xxxxxxxx \
  --scheme internet-facing \
  --type application \
  --ip-address-type ipv4

# Note: subnets must be in at least 2 different AZs
```

#### Step 3: Create Listener and Rules
```bash
# Create listener on port 80
aws elbv2 create-listener \
  --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-alb/1234567890abcdef \
  --protocol HTTP \
  --port 80 \
  --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890abcdef

# Create rule: path-based routing
aws elbv2 create-rule \
  --listener-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/my-alb/1234567890abcdef/1234567890abcdef \
  --priority 1 \
  --conditions Field=path-pattern,Values=/api/* \
  --actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/api-targets/1234567890abcdef

# Create rule: host-based routing
aws elbv2 create-rule \
  --listener-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/my-alb/1234567890abcdef/1234567890abcdef \
  --priority 2 \
  --conditions Field=host-header,Values=api.example.com \
  --actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/api-targets/1234567890abcdef
```

#### Step 4: Register Targets
```bash
# Register EC2 instances as targets
aws elbv2 register-targets \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890abcdef \
  --targets Id=i-1234567890abcdef0 Id=i-0987654321abcdef1

# Check target health
aws elbv2 describe-target-health \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890abcdef
```

#### Step 5: Configure HTTPS
```bash
# Import certificate (or use ACM)
aws elbv2 create-listener \
  --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-alb/1234567890abcdef \
  --protocol HTTPS \
  --port 443 \
  --certificates CertificateArn=arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012 \
  --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890abcdef
```

#### Step 6: Enable Sticky Sessions (Optional)
```bash
# Configure sticky sessions (session persistence)
aws elbv2 modify-target-group-attributes \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890abcdef \
  --attributes \
    Key=stickiness.enabled,Value=true \
    Key=stickiness.type,Value=lb_cookie \
    Key=stickiness.lb_cookie.duration_seconds,Value=86400
```

### Important Commands

```bash
# List load balancers
aws elbv2 describe-load-balancers

# List target groups
aws elbv2 describe-target-groups

# Check target health
aws elbv2 describe-target-health --target-group-arn <arn>

# Modify listener
aws elbv2 modify-listener \
  --listener-arn <arn> \
  --protocol HTTPS \
  --port 443

# Deregister target
aws elbv2 deregister-targets \
  --target-group-arn <arn> \
  --targets Id=i-1234567890abcdef0

# Delete load balancer
aws elbv2 delete-load-balancer --load-balancer-arn <arn>

# Describe load balancer attributes
aws elbv2 describe-load-balancer-attributes --load-balancer-arn <arn>

# Enable access logs
aws elbv2 modify-load-balancer-attributes \
  --load-balancer-arn <arn> \
  --attributes \
    Key=access_logs.s3.enabled,Value=true \
    Key=access_logs.s3.bucket,Value=my-bucket \
    Key=access_logs.s3.prefix,Value=alb-logs
```

### Architecture Diagram

```
┌────────────────────────────────────────────────────────┐
│              Internet (Users)                          │
└─────────────────────┬──────────────────────────────────┘
                      │ HTTP/HTTPS (Port 80/443)
                      ↓
         ┌────────────────────────────┐
         │  Application Load Balancer │
         │   DNS: my-alb.example.com  │
         └────────────┬───────────────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
          ↓           ↓           ↓
     ┌────────┐ ┌────────┐ ┌────────┐
     │ Health │ │ Health │ │ Health │
     │ Checks │ │ Checks │ │ Checks │
     └────┬───┘ └────┬───┘ └────┬───┘
          │          │          │
          ↓          ↓          ↓
     ┌─────────┐ ┌─────────┐ ┌─────────┐
     │ EC2 AZ1 │ │ EC2 AZ1 │ │ EC2 AZ2 │
     │Port 80  │ │Port 80  │ │Port 80  │
     └─────────┘ └─────────┘ └─────────┘
     (Healthy)   (Healthy)   (Healthy)

     Target Group: my-targets
     ├─ Protocol: HTTP
     ├─ Port: 80
     ├─ Health Check: /health every 30s
     └─ Sticky Sessions: Enabled
```

### Common Mistakes Beginners Make

1. **Creating load balancer in only 1 AZ**: Always use at least 2 AZs for HA
2. **Health check path returns error codes**: Configure health check endpoint properly
3. **Not setting up security groups properly**: Allow LB → targets traffic
4. **Forgetting SSL/TLS certificates**: Use ACM for free certificates
5. **Not enabling access logs**: Important for debugging and security
6. **Sticky sessions causing imbalance**: Use only when necessary
7. **Ignoring target group attributes**: Configure idle timeout, deregistration delay

### Interview Questions

1. **What's the difference between ALB and NLB?**
   - ALB: Layer 7 routing, best for web apps and APIs
   - NLB: Layer 4 routing, best for extreme performance and non-HTTP

2. **How do load balancers determine if a target is healthy?**
   - Send periodic HTTP requests to health check path
   - Check response status code (200-399 = healthy)
   - Mark unhealthy after X consecutive failures
   - Remove from pool until healthy again

3. **Explain sticky sessions and when to use them.**
   - Sticky sessions: Route requests from same user to same target
   - Use when: Session state stored locally on instance
   - Avoid when: Using external session store (Redis, DynamoDB)

4. **How would you scale with Auto Scaling and ELB?**
   - Create launch template with app configuration
   - Create Auto Scaling group with target group attached
   - Set scaling policies (CPU, requests per target)
   - Load balancer automatically routes to new instances

5. **What are potential bottlenecks when using ELB?**
   - Load balancer itself (rarely issue with AWS)
   - Target connection pooling
   - Uneven traffic distribution (check target health)
   - Slow application responses

### Mini Project: High-Availability Web Application

**Objective**: Create load-balanced, auto-scaled web application

**Requirements**:
- Application Load Balancer across 2 AZs
- Target group with health checks
- Auto Scaling group (2-10 instances)
- HTTPS listener with ACM certificate
- Access logging to S3
- CloudWatch alarms for unhealthy targets

**Steps**:
1. Create target group with health checks
2. Launch ALB in 2+ AZs
3. Create HTTPS listener with ACM cert
4. Create launch template (includes app code)
5. Create Auto Scaling group attached to target group
6. Configure scaling policies:
   - Scale up if CPU > 70%
   - Scale down if CPU < 30%
7. Enable ALB access logs to S3
8. Create CloudWatch alarms for:
   - Unhealthy target count
   - Target response time

---

## 7. AWS Auto Scaling

### What is Auto Scaling?
Auto Scaling automatically adjusts the number of EC2 instances (or other resources) based on demand. It launches new instances when demand increases and terminates instances when demand decreases, optimizing cost and availability.

### Why Use Auto Scaling?
**Real-World Example**: A food delivery app experiences massive spike during lunch hours. Without Auto Scaling:
- 9:00 AM: Need 10 instances
- 12:00 PM: Need 100 instances (manual scaling too slow!)
- 2:00 PM: Need 10 instances (wasted resources)

With Auto Scaling:
- Automatically scales up/down based on metrics
- No manual intervention needed
- Optimal cost + performance + availability

**Advantages**:
- Cost optimization (pay only for needed capacity)
- High availability (maintains minimum instances)
- Automatic replacement of unhealthy instances
- Scheduled scaling for predictable demand
- Smart scaling based on multiple metrics

### Key Concepts

**Auto Scaling Components**:
```
Launch Template
├─ AMI ID
├─ Instance type
├─ Security groups
├─ Key pair
└─ User data script

Auto Scaling Group (ASG)
├─ Min size: 2
├─ Max size: 10
├─ Desired capacity: 5
├─ Health check grace period: 300 seconds
└─ Termination policies: OldestLaunchTemplate, Default, etc.

Scaling Policies
├─ Target tracking (simple: maintain CPU at 70%)
├─ Step scaling (escalating actions)
└─ Scheduled scaling (fixed times)

Lifecycle Hooks
├─ Launch hook: Actions before instance becomes active
└─ Terminate hook: Actions before instance terminates
```

### Step-by-Step Setup Guide

#### Step 1: Create Launch Template
```bash
# Create launch template
aws ec2 create-launch-template \
  --launch-template-name my-app-template \
  --version-description "Web server template" \
  --launch-template-data '{
    "ImageId": "ami-0c55b159cbfafe1f0",
    "InstanceType": "t3.micro",
    "SecurityGroupIds": ["sg-xxxxxxxx"],
    "KeyName": "my-key-pair",
    "UserData": "IyEvYmluL2Jhc2gKY3VybCBodHRwczovL2dldC5kb2NrZXIuY29tIHwgYmFzaAphcHQtZ2V0IHVwZGF0ZSAteSAmJiBhcHQtZ2V0IGluc3RhbGwgLXkgZG9ja2VyLmlvCmRvY2tlciByb24gLWQgLXAgODA6ODAgbmdpbng="
  }'

# Describe launch template
aws ec2 describe-launch-templates --launch-template-names my-app-template
```

#### Step 2: Create Auto Scaling Group
```bash
# Create Auto Scaling group
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name my-asg \
  --launch-template LaunchTemplateName=my-app-template,Version='$Latest' \
  --min-size 2 \
  --max-size 10 \
  --desired-capacity 4 \
  --health-check-type ELB \
  --health-check-grace-period 300 \
  --vpc-zone-identifier "subnet-xxxxxxxx,subnet-yyyyyyyy" \
  --target-group-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890abcdef
```

#### Step 3: Create Target Tracking Scaling Policy
```bash
# Simple scaling: maintain CPU at 70%
aws autoscaling put-scaling-policy \
  --auto-scaling-group-name my-asg \
  --policy-name target-tracking-cpu \
  --policy-type TargetTrackingScaling \
  --target-tracking-configuration '{
    "TargetValue": 70.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ASGAverageCPUUtilization"
    },
    "ScaleOutCooldown": 60,
    "ScaleInCooldown": 300
  }'

# Or target requests per minute
aws autoscaling put-scaling-policy \
  --auto-scaling-group-name my-asg \
  --policy-name target-tracking-rps \
  --policy-type TargetTrackingScaling \
  --target-tracking-configuration '{
    "TargetValue": 1000.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ALBRequestCountPerTarget"
    }
  }'
```

#### Step 4: Create Step Scaling Policy
```bash
# Create alarm for high CPU
aws cloudwatch put-metric-alarm \
  --alarm-name high-cpu \
  --alarm-description "Alarm when CPU > 80%" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=AutoScalingGroupName,Value=my-asg \
  --evaluation-periods 2

# Create step scaling policy
aws autoscaling put-scaling-policy \
  --auto-scaling-group-name my-asg \
  --policy-name step-scaling-out \
  --policy-type StepScaling \
  --adjustment-type PercentChangeInCapacity \
  --metric-aggregation-type Average \
  --estimated-warmup-seconds 300 \
  --step-adjustments \
    MetricIntervalLowerBound=0,MetricIntervalUpperBound=10,AdjustmentValue=10 \
    MetricIntervalLowerBound=10,AdjustmentValue=20

# Attach alarm to policy
aws autoscaling attach-scaling-policies \
  --auto-scaling-group-name my-asg \
  --policy-arns arn:aws:autoscaling:us-east-1:123456789012:policy:12345678-1234-1234-1234-123456789012
```

#### Step 5: Create Scheduled Action
```bash
# Scale up at 12:00 PM every day (lunch rush)
aws autoscaling put-scheduled-action \
  --auto-scaling-group-name my-asg \
  --scheduled-action-name lunch-rush-scale-up \
  --recurrence "0 12 * * *" \
  --desired-capacity 20 \
  --min-size 15

# Scale down at 3:00 PM every day
aws autoscaling put-scheduled-action \
  --auto-scaling-group-name my-asg \
  --scheduled-action-name afternoon-scale-down \
  --recurrence "0 15 * * *" \
  --desired-capacity 5 \
  --min-size 2
```

#### Step 6: Create Lifecycle Hook
```bash
# Create hook for graceful shutdown
aws autoscaling put-lifecycle-hook \
  --auto-scaling-group-name my-asg \
  --lifecycle-hook-name graceful-shutdown \
  --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING \
  --default-result CONTINUE \
  --heartbeat-timeout 300 \
  --notification-target-arn arn:aws:sqs:us-east-1:123456789012:asg-termination-queue \
  --role-arn arn:aws:iam::123456789012:role/autoscaling-notification-role

# Application can then:
# 1. Receive notification via SQS
# 2. Finish current requests
# 3. Send heartbeat (extends timeout)
# 4. Complete lifecycle action
```

### Important Commands

```bash
# Describe Auto Scaling groups
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names my-asg

# Describe scaling activities
aws autoscaling describe-scaling-activities --auto-scaling-group-name my-asg

# Set desired capacity
aws autoscaling set-desired-capacity \
  --auto-scaling-group-name my-asg \
  --desired-capacity 6

# Update Auto Scaling group
aws autoscaling update-auto-scaling-group \
  --auto-scaling-group-name my-asg \
  --min-size 3 \
  --max-size 15

# Terminate instance (triggers replacement)
aws autoscaling terminate-instance-in-auto-scaling-group \
  --instance-id i-1234567890abcdef0 \
  --should-decrement-desired-capacity

# Delete Auto Scaling group
aws autoscaling delete-auto-scaling-group \
  --auto-scaling-group-name my-asg \
  --force-delete

# List scaling policies
aws autoscaling describe-scaling-policies --auto-scaling-group-name my-asg

# Describe launch templates
aws ec2 describe-launch-templates --launch-template-names my-app-template
```

### Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│         CloudWatch Metrics                          │
│  (CPU, ALB requests, custom metrics)               │
└──────────────────┬──────────────────────────────────┘
                   │
                   ↓
         ┌─────────────────────┐
         │ Scaling Policies    │
         │  1. Target Tracking │
         │  2. Step Scaling    │
         │  3. Scheduled       │
         └──────────┬──────────┘
                    │
                    ↓
         ┌──────────────────────────────┐
         │  Auto Scaling Group (my-asg) │
         │  Min: 2, Max: 10, Desired: 5 │
         └──────────┬───────────────────┘
                    │
        ┌───────────┼───────────┬─────────┐
        │           │           │         │
        ↓           ↓           ↓         ↓
    ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
    │ EC2    │ │ EC2    │ │ EC2    │ │ EC2    │
    │ AZ1-1  │ │ AZ1-2  │ │ AZ2-1  │ │ AZ2-2  │
    └────────┘ └────────┘ └────────┘ └────────┘
        │           │           │         │
        └───────────┼───────────┼─────────┘
                    │
                    ↓
         ┌──────────────────────┐
         │ Load Balancer        │
         │ Automatically adds/  │
         │ removes targets      │
         └──────────────────────┘

Launch Template:
├─ AMI: Amazon Linux 2
├─ Type: t3.micro
├─ Security Groups: web-sg
├─ User Data: Install app
└─ Key Pair: my-key
```

### Common Mistakes Beginners Make

1. **Desired > Max capacity**: Scaling won't work if desired > max
2. **Health check grace period too short**: App needs time to start
3. **Scaling policies conflicting**: Different policies triggering at once
4. **No proper termination handling**: Long-running tasks interrupted
5. **Not testing scaling**: Always test scale up and down
6. **Wrong metric for scaling**: CPU works, but ALB requests better
7. **Launch template with hardcoded values**: Makes scaling inefficient

### Interview Questions

1. **What's the difference between desired, min, and max capacity?**
   - Min: Minimum instances always running
   - Max: Maximum instances allowed
   - Desired: Target number of instances

2. **How does Auto Scaling detect unhealthy instances?**
   - ELB health check: Instance fails health check
   - EC2 health check: System/instance status checks fail
   - Custom: Application reports unhealthy via API

3. **Explain the difference between scaling policies.**
   - Target tracking: Simplest, maintain metric at target (70% CPU)
   - Step scaling: Complex escalating actions based on thresholds
   - Scheduled: Fixed times (lunch rush at 12:00 PM)

4. **How would you implement graceful shutdown?**
   - Create lifecycle hook on EC2_INSTANCE_TERMINATING
   - Application receives notification via SNS/SQS
   - Application finishes current requests
   - Send complete-lifecycle-action to continue termination

5. **What causes excessive scaling up and down?**
   - Metric too volatile (use averages)
   - Cooldown period too short
   - Scaling thresholds too close together

### Mini Project: Auto-Scaled E-Commerce Platform

**Objective**: Create auto-scaling setup for traffic patterns

**Requirements**:
- Launch template with web server
- Auto Scaling group (2-50 instances)
- Target tracking (CPU at 65%)
- Scheduled scaling for peak hours
- Lifecycle hooks for graceful shutdown
- CloudWatch dashboards tracking scaling

**Steps**:
1. Create launch template with app installation
2. Create Auto Scaling group (min: 2, max: 50, desired: 5)
3. Configure target tracking policy (CPU 65%)
4. Add scheduled actions:
   - 11:00 AM: Scale to 30 instances (lunch)
   - 2:00 PM: Scale back to 5 instances
5. Implement graceful shutdown:
   - Create SQS queue for termination notifications
   - Create lifecycle hook
   - Application drains connections before termination
6. Monitor scaling activities via CloudWatch
7. Test scaling with load testing

---

## 8. Amazon CloudWatch

### What is CloudWatch?
CloudWatch is AWS's monitoring and observability service. It collects metrics from AWS resources, stores logs from applications, detects anomalies, and triggers alarms based on thresholds.

### Why Use CloudWatch?
**Real-World Example**: A SaaS platform experiences degradation. Without CloudWatch:
- Users complain, but you don't know why
- Application logs are scattered
- Performance metrics are unknown

With CloudWatch:
- See CPU, memory, network metrics in real-time
- View application logs from all servers in one place
- Set alarms to alert on issues
- Create dashboards for executive reporting
- Identify performance bottlenecks

**Advantages**:
- Unified monitoring and logging
- Real-time metrics (detailed monitoring)
- Automatic anomaly detection
- Metric math for complex calculations
- Log insights with powerful queries
- Cross-AWS-service integration

### Key Concepts

**CloudWatch Metrics**:
```
Metric: CPUUtilization
├─ Namespace: AWS/EC2
├─ Dimensions: InstanceId=i-1234567, AZ=us-east-1a
├─ DataPoints: 72%, 75%, 68%, 79%
├─ Timestamp: 2024-01-15 10:00:00
└─ Granularity: 1 minute (standard), 10 seconds (detailed)

CloudWatch Logs:
├─ Log Group: /aws/ec2/application
├─ Log Streams: i-1234567890abcdef0 (one per instance)
└─ Log Events: Timestamped messages

Alarms:
├─ Metric: CPUUtilization > 80%
├─ Evaluation: 2 periods of 5 minutes
├─ Action: SNS notification, Auto Scaling, etc.
└─ State: OK, ALARM, INSUFFICIENT_DATA
```

### Step-by-Step Setup Guide

#### Step 1: Publish Custom Metrics
```bash
# Install CloudWatch agent on EC2
aws s3 cp s3://amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm . && rpm -U ./amazon-cloudwatch-agent.rpm

# Create CloudWatch agent configuration
cat > /opt/aws/amazon-cloudwatch-agent/etc/config.json << 'EOF'
{
  "metrics": {
    "namespace": "CustomApp",
    "metrics_collected": {
      "cpu": {
        "measurement": [
          {
            "name": "cpu_usage_idle",
            "rename": "CPU_IDLE",
            "unit": "Percent"
          }
        ],
        "totalcpu": false,
        "metrics_collection_interval": 60
      },
      "mem": {
        "measurement": [
          {
            "name": "mem_used_percent",
            "rename": "MEM_USED",
            "unit": "Percent"
          }
        ],
        "metrics_collection_interval": 60
      },
      "disk": {
        "measurement": [
          {
            "name": "used_percent",
            "rename": "DISK_USED",
            "unit": "Percent"
          }
        ],
        "metrics_collection_interval": 60,
        "resources": ["/"]
      }
    }
  }
}
EOF

# Start agent
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/etc/config.json
```

#### Step 2: Publish Custom Metrics via CLI
```bash
# Publish custom metric
aws cloudwatch put-metric-data \
  --namespace "MyApp" \
  --metric-name "ActiveUsers" \
  --value 5432 \
  --unit Count \
  --timestamp 2024-01-15T10:00:00Z

# Publish metric with dimensions
aws cloudwatch put-metric-data \
  --namespace "MyApp" \
  --metric-name "OrderProcessingTime" \
  --dimensions Environment=Production,Region=us-east-1 \
  --value 245 \
  --unit Milliseconds
```

#### Step 3: Create CloudWatch Log Group
```bash
# Create log group
aws logs create-log-group --log-group-name /aws/lambda/my-function

# Create log stream
aws logs create-log-stream \
  --log-group-name /aws/lambda/my-function \
  --log-stream-name 2024/01/15/[$LATEST]abcdef1234567890

# Put log events
aws logs put-log-events \
  --log-group-name /aws/lambda/my-function \
  --log-stream-name "2024/01/15/[$LATEST]abcdef1234567890" \
  --log-events timestamp=$(date +%s000),message="Application started successfully"

# Set retention policy (30 days)
aws logs put-retention-policy \
  --log-group-name /aws/lambda/my-function \
  --retention-in-days 30
```

#### Step 4: Create CloudWatch Alarm
```bash
# Create alarm: High CPU
aws cloudwatch put-metric-alarm \
  --alarm-name high-cpu-alarm \
  --alarm-description "Alert when CPU > 80%" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:my-topic \
  --ok-actions arn:aws:sns:us-east-1:123456789012:my-topic

# Create alarm: Low CPU (scale down)
aws cloudwatch put-metric-alarm \
  --alarm-name low-cpu-alarm \
  --alarm-description "Alert when CPU < 20%" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 20 \
  --comparison-operator LessThanThreshold \
  --evaluation-periods 3 \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0
```

#### Step 5: Create CloudWatch Dashboard
```bash
# Create dashboard
aws cloudwatch put-dashboard \
  --dashboard-name MyAppDashboard \
  --dashboard-body '{
    "widgets": [
      {
        "type": "metric",
        "properties": {
          "metrics": [
            ["AWS/EC2", "CPUUtilization", {"stat": "Average"}],
            ["AWS/EC2", "NetworkIn", {"stat": "Sum"}],
            ["AWS/EC2", "NetworkOut", {"stat": "Sum"}]
          ],
          "period": 300,
          "stat": "Average",
          "region": "us-east-1",
          "title": "EC2 Instance Metrics",
          "yAxis": {"left": {"min": 0, "max": 100}}
        }
      },
      {
        "type": "log",
        "properties": {
          "query": "fields @timestamp, @message | stats count() by bin(5m)",
          "region": "us-east-1",
          "title": "Log Insights Query"
        }
      }
    ]
  }'
```

#### Step 6: Create Log Insights Queries
```bash
# Query: Find errors in logs
aws logs start-query \
  --log-group-name /aws/lambda/my-function \
  --start-time $(date -d '1 hour ago' +%s) \
  --end-time $(date +%s) \
  --query-string 'fields @timestamp, @message | filter @message like /ERROR/ | stats count()'

# Query: Performance analysis
aws logs start-query \
  --log-group-name /aws/ec2/application \
  --start-time $(date -d '24 hours ago' +%s) \
  --end-time $(date +%s) \
  --query-string 'fields @duration | stats pct(@duration, 50), pct(@duration, 95), pct(@duration, 99)'

# Query: Traffic by user
aws logs start-query \
  --log-group-name /aws/ec2/application \
  --query-string 'fields @timestamp, userId, @message | stats count() as requests by userId | sort requests desc'
```

### Important Commands

```bash
# Get metric statistics
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --start-time 2024-01-15T10:00:00Z \
  --end-time 2024-01-15T12:00:00Z \
  --period 300 \
  --statistics Average,Maximum,Minimum

# List metrics
aws cloudwatch list-metrics --namespace AWS/EC2

# Delete alarm
aws cloudwatch delete-alarms --alarm-names my-alarm

# Describe alarms
aws cloudwatch describe-alarms --alarm-names my-alarm

# Get alarm history
aws cloudwatch describe-alarm-history --alarm-name my-alarm

# Create anomaly detector
aws cloudwatch put-anomaly-detector \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --stat Average

# Filter log events
aws logs filter-log-events \
  --log-group-name /aws/lambda/my-function \
  --filter-pattern "ERROR"

# Describe log groups
aws logs describe-log-groups --log-group-name-prefix /aws/lambda
```

### Architecture Diagram

```
┌──────────────────────────────────────────────────────┐
│         AWS Resources                                │
│  ┌─────────┐ ┌──────────┐ ┌────────┐ ┌────────┐    │
│  │EC2      │ │ RDS      │ │Lambda  │ │ ECS    │    │
│  └────┬────┘ └────┬─────┘ └───┬────┘ └───┬────┘    │
│       │           │           │          │          │
└───────┼───────────┼───────────┼──────────┼──────────┘
        │           │           │          │
        └───────────┼───────────┼──────────┘
                    ↓
         ┌──────────────────────┐
         │  CloudWatch Agent    │
         │  (Custom Metrics)    │
         └──────────┬───────────┘
                    │
    ┌───────────────┼────────────────┐
    ↓               ↓                ↓
┌────────────┐ ┌──────────────┐ ┌────────────┐
│  Metrics   │ │ Logs         │ │  Events    │
│ (CPU, Mem) │ │ (Application)│ │ (Alarms)   │
└────────┬───┘ └────┬─────────┘ └────┬───────┘
         │          │                │
         └──────────┼────────────────┘
                    ↓
         ┌──────────────────────┐
         │   CloudWatch         │
         │ (Central Dashboard)  │
         └──────────┬───────────┘
                    │
        ┌───────────┼────────────┐
        ↓           ↓            ↓
    ┌────────┐ ┌────────┐ ┌──────────┐
    │Alarms  │ │Insights│ │ Reports  │
    └────┬───┘ └────────┘ └──────┬───┘
         │                       │
         ├─→ SNS Topic           └─→ Email/Slack
         ├─→ Auto Scaling        └─→ Dashboards
         └─→ Lambda
```

### Common Mistakes Beginners Make

1. **Creating too many custom metrics**: Keep metric count manageable
2. **Setting alarm thresholds without baseline**: Collect data first
3. **Not retaining logs long enough**: Set appropriate retention policy
4. **Ignoring CloudWatch costs**: Be careful with detailed monitoring
5. **Not using log filters**: Hard to find issues in massive logs
6. **Alarms pointing to wrong SNS topic**: Test notifications
7. **Not setting up dashboards**: Can't see overall health

### Interview Questions

1. **What's the difference between standard and detailed monitoring?**
   - Standard: 5-minute granularity, free
   - Detailed: 1-minute granularity, additional cost

2. **How do you optimize CloudWatch costs?**
   - Use standard monitoring (5 min) instead of detailed
   - Filter logs before storing (use subscriptions)
   - Set appropriate log retention (30-90 days)
   - Use metric math instead of custom metrics

3. **Explain CloudWatch Logs Insights and use cases.**
   - Powerful query language for log analysis
   - Find errors, analyze performance, user behavior
   - Create metrics from logs for alerting

4. **How would you troubleshoot an underperforming application?**
   - Check CloudWatch metrics (CPU, memory, network)
   - Review application logs for errors
   - Analyze request/response times
   - Check RDS slow query log
   - Use X-Ray for distributed tracing

5. **What's an anomaly detector and how is it useful?**
   - Learns metric patterns automatically
   - Detects deviations from baseline
   - Triggers alarms on anomalies (not just thresholds)
   - Better than static thresholds for dynamic workloads

### Mini Project: Complete Monitoring Solution

**Objective**: Implement comprehensive monitoring for multi-tier app

**Requirements**:
- CloudWatch agent on EC2 for OS metrics
- Custom metrics from application
- Log collection from all tiers
- Alarms for critical metrics
- Dashboard for executives
- Log Insights queries for troubleshooting

**Steps**:
1. Install CloudWatch agent on all EC2 instances
2. Configure agent to collect:
   - CPU utilization
   - Memory usage
   - Disk usage
   - Network metrics
3. Create Log Groups for:
   - Web tier logs (/aws/ec2/web)
   - App tier logs (/aws/ec2/app)
   - Database logs (/aws/rds/db)
4. Create alarms:
   - High CPU > 80% (2 periods)
   - High memory > 85%
   - RDS connections > 80
   - Error rate > 1%
5. Create dashboard showing:
   - Instance health
   - Application metrics
   - Error rate trend
   - Response time P99
6. Create Log Insights queries:
   - Error analysis
   - Performance analysis
   - User behavior analysis

---

## 9. AWS Lambda

### What is Lambda?
Lambda is AWS's serverless compute service. Instead of managing servers, you upload code and Lambda automatically scales, runs, and manages the infrastructure. You pay only for the computing time you consume.

### Why Use Lambda?
**Real-World Example**: An image processing startup receives varying upload volumes:
- 9:00 AM: 10 uploads/hour
- 2:00 PM: 1,000 uploads/hour (viral content)
- 9:00 PM: 5 uploads/hour

With Lambda:
- Automatically scales to handle 1,000 uploads
- Scales back down when demand decreases
- No servers to manage
- Pay only for actual processing time

**Advantages**:
- No server management
- Automatic scaling
- Pay-per-use pricing
- Sub-second billing granularity
- Integrated with AWS ecosystem
- Event-driven architecture

### Key Concepts

**Lambda Components**:
```
Lambda Function
├─ Runtime: Python, Node.js, Java, Go, etc.
├─ Handler: Entry point (lambda_function.lambda_handler)
├─ Memory: 128MB - 10GB (CPU scales with memory)
├─ Timeout: 1 second - 15 minutes
├─ Environment variables: Configuration
├─ Layers: Shared code/libraries
└─ Version & Alias: Version management

Triggers (Event Sources):
├─ API Gateway (HTTP requests)
├─ S3 (object upload/deletion)
├─ DynamoDB (stream records)
├─ SNS (notifications)
├─ SQS (queue messages)
├─ CloudWatch (scheduled events)
├─ EventBridge (complex event routing)
└─ Direct invocation (SDK/CLI)

Execution Role:
├─ IAM role with permissions
├─ Allows Lambda to access AWS services
└─ Example: Read from S3, write to DynamoDB
```

**Cold Start vs Warm Start**:
- Cold start: First invocation or after idle period (~1-2 seconds)
- Warm start: Subsequent invocations (~milliseconds)
- Provisioned concurrency: Pre-warmed functions (cost more)

### Step-by-Step Setup Guide

#### Step 1: Create IAM Role for Lambda
```bash
# Create role
aws iam create-role \
  --role-name lambda-execution-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Attach basic execution policy (CloudWatch logs)
aws iam attach-role-policy \
  --role-name lambda-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Create custom policy for S3 access
cat > s3-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "s3:GetObject",
      "s3:PutObject"
    ],
    "Resource": "arn:aws:s3:::my-bucket/*"
  }]
}
EOF

aws iam put-role-policy \
  --role-name lambda-execution-role \
  --policy-name lambda-s3-policy \
  --policy-document file://s3-policy.json
```

#### Step 2: Create Lambda Function (Python)
```bash
# Create deployment package
mkdir lambda-function
cd lambda-function

# Create lambda function
cat > lambda_function.py << 'EOF'
import json
import boto3
import base64
from PIL import Image
import io

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Process S3 image uploads
    """
    try:
        # Parse S3 event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Download image
        response = s3_client.get_object(Bucket=bucket, Key=key)
        image_data = response['Body'].read()
        
        # Process image (resize)
        image = Image.open(io.BytesIO(image_data))
        image.thumbnail((200, 200))
        
        # Save processed image
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG')
        buffer.seek(0)
        
        output_key = f"processed/{key}"
        s3_client.put_object(
            Bucket=bucket,
            Key=output_key,
            Body=buffer.getvalue()
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Processed image: {output_key}')
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
EOF

# Install dependencies
pip install Pillow -t .

# Create deployment package
zip -r lambda-function.zip .
```

#### Step 3: Deploy Lambda Function
```bash
# Create function
aws lambda create-function \
  --function-name image-processor \
  --runtime python3.11 \
  --role arn:aws:iam::123456789012:role/lambda-execution-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://lambda-function.zip \
  --timeout 60 \
  --memory-size 256 \
  --environment Variables="{LOG_LEVEL=INFO}"
```

#### Step 4: Create S3 Trigger
```bash
# Grant S3 permission to invoke Lambda
aws lambda add-permission \
  --function-name image-processor \
  --statement-id AllowS3Invoke \
  --action lambda:InvokeFunction \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::my-bucket

# Create S3 event notification
aws s3api put-bucket-notification-configuration \
  --bucket my-bucket \
  --notification-configuration '{
    "LambdaFunctionConfigurations": [{
      "LambdaFunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:image-processor",
      "Events": ["s3:ObjectCreated:*"],
      "Filter": {"Key": {"FilterRules": [{"Name": "prefix", "Value": "uploads/"}]}}
    }]
  }'
```

#### Step 5: Create API Gateway Trigger
```bash
# Create REST API
aws apigateway create-rest-api \
  --name image-api \
  --description "Image processing API"

# Get API ID
API_ID=$(aws apigateway get-rest-apis --query 'items[0].id' --output text)

# Get root resource ID
ROOT_ID=$(aws apigateway get-resources --rest-api-id $API_ID --query 'items[0].id' --output text)

# Create /process resource
RESOURCE_ID=$(aws apigateway create-resource \
  --rest-api-id $API_ID \
  --parent-id $ROOT_ID \
  --path-part process \
  --query 'id' --output text)

# Create POST method
aws apigateway put-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method POST \
  --authorization-type NONE

# Create Lambda integration
aws apigateway put-integration \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method POST \
  --type AWS_PROXY \
  --integration-http-method POST \
  --uri arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:image-processor/invocations
```

#### Step 6: Configure Lambda Layers (Shared Code)
```bash
# Create layer
mkdir python
pip install Pillow -t python/lib/python3.11/site-packages

zip -r pillow-layer.zip python

aws lambda publish-layer-version \
  --layer-name pillow-library \
  --zip-file fileb://pillow-layer.zip \
  --compatible-runtimes python3.11

# Update function to use layer
aws lambda update-function-configuration \
  --function-name image-processor \
  --layers arn:aws:lambda:us-east-1:123456789012:layer:pillow-library:1
```

### Important Commands

```bash
# Invoke function
aws lambda invoke \
  --function-name image-processor \
  --payload '{"test": "data"}' \
  response.json

# List functions
aws lambda list-functions

# Get function details
aws lambda get-function --function-name image-processor

# Update function code
aws lambda update-function-code \
  --function-name image-processor \
  --zip-file fileb://lambda-function.zip

# Create alias
aws lambda create-alias \
  --function-name image-processor \
  --name production \
  --function-version 5

# Update environment variables
aws lambda update-function-configuration \
  --function-name image-processor \
  --environment Variables="{LOG_LEVEL=DEBUG,MAX_SIZE=1000}"

# Set reserved concurrency
aws lambda put-function-concurrency \
  --function-name image-processor \
  --reserved-concurrent-executions 100

# Delete function
aws lambda delete-function --function-name image-processor

# View logs
aws logs tail /aws/lambda/image-processor --follow
```

### Architecture Diagram

```
┌──────────────────────────────────────────────────┐
│          Event Sources                           │
│  ┌────────┐ ┌─────────┐ ┌────────┐ ┌──────────┐│
│  │S3      │ │API GW   │ │SNS     │ │CloudWatch││
│  │Upload  │ │Request  │ │Message │ │Scheduled ││
│  └────┬───┘ └────┬────┘ └───┬────┘ └─────┬────┘│
└───────┼──────────┼───────────┼───────────┼─────┘
        │          │           │           │
        └──────────┼───────────┼───────────┘
                   ↓
        ┌─────────────────────┐
        │  Lambda Function    │
        │  (image-processor)  │
        │                     │
        │ Memory: 256MB       │
        │ Timeout: 60s        │
        │ Concurrency: 100    │
        └──────────┬──────────┘
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     ┌────────┐ ┌────────┐ ┌───────┐
     │CloudWatch│ │ S3    │ │RDS    │
     │ Logs   │ │Results │ │Record │
     └────────┘ └────────┘ └───────┘
```

### Common Mistakes Beginners Make

1. **Functions too large**: Break into smaller, focused functions
2. **No error handling**: Always try-catch and return proper responses
3. **Not using environment variables**: Hardcoding values is bad
4. **Ignoring cold starts**: Can impact user experience
5. **No timeout configuration**: Functions run indefinitely = cost!
6. **Not monitoring**: Use CloudWatch logs and metrics
7. **Inefficient IAM roles**: Grant minimum permissions needed

### Interview Questions

1. **Explain cold starts and how to minimize them.**
   - Cold start: ~1-2 seconds when Lambda needs to initialize
   - Minimize by: Using provisioned concurrency, optimizing code size, using Java with AOT compilation

2. **How do you handle long-running tasks in Lambda?**
   - Lambda max timeout: 15 minutes
   - For longer: Use Step Functions to orchestrate multiple functions
   - Or use SQS queue to trigger job processor

3. **What's the best way to handle errors in Lambda?**
   - Try-catch all code
   - Return structured error responses
   - Log errors to CloudWatch
   - Use Dead Letter Queue for failed async invocations

4. **How do you scale Lambda functions?**
   - Automatic: AWS scales based on events
   - Concurrency limit: Account-wide soft limit (1000)
   - Reserved concurrency: Guarantee X concurrent executions
   - Provisioned concurrency: Pre-warm X functions

5. **Explain Lambda layers and their use cases.**
   - Shared code/libraries across functions
   - Reduces code duplication
   - Example: Common utilities, SDKs, dependencies

### Mini Project: Image Processing Pipeline

**Objective**: Build serverless image processing service

**Requirements**:
- Lambda function for image resize
- S3 trigger on image upload
- Write processed images back to S3
- API Gateway endpoint for manual processing
- CloudWatch logs for troubleshooting
- Error handling with DLQ

**Steps**:
1. Create Lambda execution role with S3 permissions
2. Create Lambda function:
   - Accept image from S3 event
   - Resize image
   - Save to processed folder
3. Add S3 upload trigger
4. Create API Gateway:
   - POST /process endpoint
   - Accept image URL parameter
5. Implement error handling:
   - CloudWatch logs
   - SNS notification on errors
6. Test:
   - Upload images via S3
   - Call API endpoint
   - Verify processed images

---

## 10. Amazon ECS (Elastic Container Service)

### What is ECS?
ECS is AWS's container orchestration service for running Docker containers at scale. It manages container deployment, scheduling, and lifecycle without needing to manage Kubernetes.

### Why Use ECS?
**Real-World Example**: A microservices platform needs to run 50 microservices across 20 servers. With ECS:
- Define container image and resources needed
- ECS automatically:
  - Places containers on best servers
  - Manages scaling
  - Handles failures with restarts
  - Manages networking and load balancing

**Advantages**:
- No Kubernetes complexity
- Deep AWS integration
- Multiple launch options (EC2, Fargate, on-premises)
- Task-level IAM roles
- CloudWatch integration
- Service discovery

### Key Concepts

**ECS Components**:
```
Task Definition (like Docker Compose)
├─ Container image: myrepo/myapp:latest
├─ CPU: 256
├─ Memory: 512 MB
├─ Port mappings: 8080:80
├─ Environment variables
└─ IAM task role

ECS Cluster
├─ Collection of resources
├─ EC2 instances (managed by you)
├─ Or Fargate (serverless)
└─ Can span multiple AZs

ECS Service
├─ Long-running task
├─ Desired count: 3 replicas
├─ Load balancer integration
├─ Auto Scaling
└─ Service discovery

ECS Task
└─ Running instance of task definition
```

**Launch Types**:
- EC2: You manage EC2 instances, more control
- Fargate: Serverless, no instance management
- EXTERNAL: On-premises servers

### Step-by-Step Setup Guide

#### Step 1: Create ECS Cluster
```bash
# Create cluster
aws ecs create-cluster \
  --cluster-name my-app-cluster \
  --default-capacity-provider-strategy \
    capacityProvider=FARGATE,weight=1,base=2
```

#### Step 2: Create Task Definition
```bash
# Create task definition file
cat > task-definition.json << 'EOF'
{
  "family": "my-app",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "containerDefinitions": [
    {
      "name": "my-app",
      "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest",
      "portMappings": [
        {
          "containerPort": 80,
          "hostPort": 80,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "ENV",
          "value": "production"
        },
        {
          "name": "LOG_LEVEL",
          "value": "info"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/my-app",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "taskRoleArn": "arn:aws:iam::123456789012:role/ecs-task-role",
  "executionRoleArn": "arn:aws:iam::123456789012:role/ecs-task-execution-role"
}
EOF

# Register task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json
```

#### Step 3: Create IAM Roles
```bash
# Create task execution role (allows pulling images, logs)
aws iam create-role \
  --role-name ecs-task-execution-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "ecs-tasks.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

aws iam attach-role-policy \
  --role-name ecs-task-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy

# Create task role (for app permissions)
aws iam create-role \
  --role-name ecs-task-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "ecs-tasks.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Add policy for S3 access
aws iam put-role-policy \
  --role-name ecs-task-role \
  --policy-name s3-access \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }]
  }'
```

#### Step 4: Create CloudWatch Log Group
```bash
# Create log group
aws logs create-log-group --log-group-name /ecs/my-app

# Set retention
aws logs put-retention-policy \
  --log-group-name /ecs/my-app \
  --retention-in-days 7
```

#### Step 5: Create ECS Service
```bash
# Create service
aws ecs create-service \
  --cluster my-app-cluster \
  --service-name my-app-service \
  --task-definition my-app:1 \
  --desired-count 3 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={
    subnets=[subnet-12345678,subnet-87654321],
    securityGroups=[sg-12345678],
    assignPublicIp=DISABLED
  }" \
  --load-balancers "[{
    targetGroupArn=arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-app/1234567890abcdef,
    containerName=my-app,
    containerPort=80
  }]"
```

#### Step 6: Configure Auto Scaling
```bash
# Create Auto Scaling target
aws application-autoscaling register-scalable-target \
  --service-namespace ecs \
  --resource-id service/my-app-cluster/my-app-service \
  --scalable-dimension ecs:service:DesiredCount \
  --min-capacity 2 \
  --max-capacity 10

# Create scaling policy (target tracking)
aws application-autoscaling put-scaling-policy \
  --policy-name ecs-scaling \
  --service-namespace ecs \
  --resource-id service/my-app-cluster/my-app-service \
  --scalable-dimension ecs:service:DesiredCount \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration '{
    "TargetValue": 70.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ECSServiceAverageCPUUtilization"
    },
    "ScaleOutCooldown": 60,
    "ScaleInCooldown": 300
  }'
```

### Important Commands

```bash
# List clusters
aws ecs list-clusters

# List services
aws ecs list-services --cluster my-app-cluster

# Describe service
aws ecs describe-services \
  --cluster my-app-cluster \
  --services my-app-service

# List tasks
aws ecs list-tasks --cluster my-app-cluster --service-name my-app-service

# Describe tasks
aws ecs describe-tasks \
  --cluster my-app-cluster \
  --tasks arn:aws:ecs:us-east-1:123456789012:task/my-app-cluster/abcdef1234567890

# Update service
aws ecs update-service \
  --cluster my-app-cluster \
  --service my-app-service \
  --desired-count 5

# Update task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

# Force new deployment
aws ecs update-service \
  --cluster my-app-cluster \
  --service my-app-service \
  --force-new-deployment

# View logs
aws logs tail /ecs/my-app --follow
```

### Architecture Diagram

```
┌────────────────────────────────────────────────────┐
│           ECS Cluster: my-app-cluster            │
├────────────────────────────────────────────────────┤
│                                                    │
│  Service: my-app-service (desired: 3)             │
│  ├─ Task 1 (AZ-1)                                │
│  │  └─ Container: my-app:latest                   │
│  │     ├─ CPU: 256                                │
│  │     ├─ Memory: 512 MB                          │
│  │     └─ Port: 80                                │
│  │                                                │
│  ├─ Task 2 (AZ-1)                                │
│  │  └─ Container: my-app:latest                   │
│  │                                                │
│  └─ Task 3 (AZ-2)                                │
│     └─ Container: my-app:latest                   │
│                                                    │
│  Auto Scaling:                                    │
│  ├─ Min: 2 tasks                                 │
│  ├─ Max: 10 tasks                                │
│  └─ Target CPU: 70%                              │
│                                                    │
│  Launch Type: FARGATE                            │
│  ├─ No EC2 management needed                     │
│  ├─ VPC integration                              │
│  └─ Security groups: sg-12345678                 │
│                                                    │
│  Load Balancer Integration:                      │
│  └─ ALB automatically routes to tasks            │
│                                                    │
└────────────────────────────────────────────────────┘
         ↓
    CloudWatch Logs: /ecs/my-app
    ├─ Task execution logs
    ├─ Container stdout/stderr
    └─ Application logs
```

### Common Mistakes Beginners Make

1. **Not using task IAM roles**: Give containers only needed permissions
2. **Insufficient memory/CPU**: Tasks OOM or get throttled
3. **No load balancer integration**: Manual traffic routing is error-prone
4. **Ignoring container logs**: Can't troubleshoot without logs
5. **Not using service discovery**: Makes microservices communication hard
6. **Forgetting about secrets**: Don't hardcode sensitive data
7. **No health checks**: Failed tasks aren't replaced

### Interview Questions

1. **What's the difference between EC2 and Fargate launch types?**
   - EC2: You manage instances, more control
   - Fargate: Serverless, no instance management

2. **How do you manage application secrets in ECS?**
   - Use AWS Secrets Manager
   - Pass via task definition as secret environment variables
   - Application retrieves secrets at runtime

3. **Explain ECS Service discovery and why it's important.**
   - Microservices need to communicate with each other
   - Service discovery maintains DNS records
   - Automatic registration/deregistration of tasks

4. **How would you perform a blue-green deployment in ECS?**
   - Create new task definition version
   - Create second service pointing to new version
   - Switch load balancer between services
   - Or use CodeDeploy for automated deployment

5. **What's the relationship between Task Definition and Task?**
   - Task Definition: Blueprint (like Docker Compose)
   - Task: Running instance of task definition
   - Like class vs object in programming

### Mini Project: Microservices Platform

**Objective**: Deploy multiple microservices using ECS

**Requirements**:
- Frontend service (Node.js)
- API service (Python)
- Database service (RDS)
- All services behind load balancer
- Service discovery for inter-service communication
- CloudWatch logging for all services
- Auto Scaling based on CPU

**Steps**:
1. Create ECS cluster (Fargate)
2. Create ECR repositories for each service
3. Build and push Docker images
4. Create task definitions:
   - Frontend task (port 3000)
   - API task (port 5000)
5. Create load balancer with 2 target groups
6. Create ECS services for each microservice
7. Configure service discovery
8. Set up Auto Scaling for each service
9. Create CloudWatch dashboards for monitoring

---

## 11. Amazon EKS (Elastic Kubernetes Service)

### What is EKS?
EKS is AWS's managed Kubernetes service. It handles Kubernetes control plane management while you manage worker nodes. Use EKS when you need Kubernetes's advanced features and multi-cloud portability.

### Why Use EKS vs ECS?
**ECS Advantages**:
- AWS-native, simpler learning curve
- Easier to start with small deployments
- Better AWS integration
- Lower operational overhead

**EKS Advantages**:
- Kubernetes standard (portable)
- Larger ecosystem and community
- Advanced features (Network Policies, RBAC, CRDs)
- Multi-cloud strategy
- Larger organizations standardize on Kubernetes

### Key Concepts

**EKS Architecture**:
```
EKS Control Plane (AWS Managed)
├─ API Server
├─ etcd (state storage)
├─ Controller Manager
└─ Scheduler

Worker Nodes (You Manage)
├─ EC2 instances or Fargate pods
├─ kubelet (node agent)
├─ container runtime (Docker)
└─ kube-proxy

Add-ons:
├─ VPC CNI (networking)
├─ CoreDNS (service discovery)
├─ kube-proxy (network routing)
├─ Ingress Controller (external access)
└─ Metrics Server (monitoring)
```

**Kubernetes Resources**:
- Pod: Smallest deployable unit (one or more containers)
- Deployment: Manages pods (scaling, rolling updates)
- Service: Exposes pods internally/externally
- ConfigMap: Configuration (non-secret)
- Secret: Sensitive data (passwords, tokens)
- Ingress: Routes external HTTP(S) to services

### Step-by-Step Setup Guide

#### Step 1: Create EKS Cluster
```bash
# Create IAM role for EKS cluster
aws iam create-role \
  --role-name eks-service-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "eks.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

aws iam attach-role-policy \
  --role-name eks-service-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSServiceRolePolicy

# Create security group for cluster
aws ec2 create-security-group \
  --group-name eks-cluster-sg \
  --description "Security group for EKS cluster" \
  --vpc-id vpc-xxxxxxxx

# Create EKS cluster
aws eks create-cluster \
  --name my-app-cluster \
  --version 1.27 \
  --role-arn arn:aws:iam::123456789012:role/eks-service-role \
  --resources-vpc-config \
    subnetIds=subnet-12345678,subnet-87654321 \
    securityGroupIds=sg-12345678

# Wait for cluster to be ACTIVE (5-10 minutes)
aws eks describe-cluster --name my-app-cluster --query 'cluster.status'
```

#### Step 2: Create Node Group
```bash
# Create IAM role for nodes
aws iam create-role \
  --role-name eks-node-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "ec2.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Attach node policies
aws iam attach-role-policy \
  --role-name eks-node-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy

aws iam attach-role-policy \
  --role-name eks-node-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy

aws iam attach-role-policy \
  --role-name eks-node-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly

# Create node group
aws eks create-nodegroup \
  --cluster-name my-app-cluster \
  --nodegroup-name my-nodegroup \
  --subnets subnet-12345678 subnet-87654321 \
  --node-role arn:aws:iam::123456789012:role/eks-node-role \
  --instance-types t3.medium \
  --scaling-config minSize=2,maxSize=10,desiredSize=3
```

#### Step 3: Configure kubectl
```bash
# Update kubeconfig
aws eks update-kubeconfig --name my-app-cluster

# Verify connection
kubectl get nodes
# Output:
# NAME                          STATUS   ROLES    AGE
# ip-10-0-1-10.ec2.internal    Ready    <none>   2m
# ip-10-0-1-20.ec2.internal    Ready    <none>   2m
```

#### Step 4: Deploy Application
```bash
# Create namespace
kubectl create namespace my-app

# Create deployment manifest
cat > deployment.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  namespace: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
EOF

# Apply deployment
kubectl apply -f deployment.yaml

# Create service
cat > service.yaml << 'EOF'
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
  namespace: my-app
spec:
  selector:
    app: my-app
  type: LoadBalancer
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
EOF

kubectl apply -f service.yaml

# Get service details
kubectl get service -n my-app
```

#### Step 5: Configure Auto Scaling
```bash
# Create cluster autoscaler deployment
# Install Helm first if not already installed
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Add autoscaler Helm repo
helm repo add autoscaling https://kubernetes.github.io/autoscaler
helm repo update

# Install cluster autoscaler
helm install cluster-autoscaler autoscaling/cluster-autoscaler \
  --namespace kube-system \
  --set autoDiscovery.clusterName=my-app-cluster \
  --set awsRegion=us-east-1

# Create HPA (Horizontal Pod Autoscaler)
cat > hpa.yaml << 'EOF'
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
  namespace: my-app
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
EOF

kubectl apply -f hpa.yaml
```

#### Step 6: Install Monitoring
```bash
# Install Prometheus and Grafana using Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Install Prometheus
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace

# Port forward to Grafana
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80
# Access at http://localhost:3000 (admin/prom-operator)
```

### Important Commands

```bash
# Get cluster info
aws eks describe-cluster --name my-app-cluster

# List node groups
aws eks list-nodegroups --cluster-name my-app-cluster

# Update cluster
aws eks update-cluster-version --name my-app-cluster --kubernetes-version 1.28

# Get pods
kubectl get pods -n my-app

# Get deployments
kubectl get deployments -n my-app

# Get services
kubectl get services -n my-app

# Describe pod
kubectl describe pod <pod-name> -n my-app

# View pod logs
kubectl logs <pod-name> -n my-app

# Port forward to service
kubectl port-forward -n my-app svc/my-app-service 8080:80

# Scale deployment
kubectl scale deployment my-app --replicas=5 -n my-app

# Update image
kubectl set image deployment/my-app \
  my-app=123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:v2 \
  -n my-app

# Rollout status
kubectl rollout status deployment/my-app -n my-app

# Rollback deployment
kubectl rollout undo deployment/my-app -n my-app
```

### Architecture Diagram

```
┌────────────────────────────────────────────────────┐
│         EKS Cluster: my-app-cluster               │
├────────────────────────────────────────────────────┤
│                                                    │
│  Control Plane (AWS Managed)                      │
│  ├─ API Server                                    │
│  ├─ etcd (state)                                  │
│  ├─ Controllers                                   │
│  └─ Scheduler                                     │
│                                                    │
├────────────────────────────────────────────────────┤
│                                                    │
│  Node Group: my-nodegroup                         │
│  ├─ Node 1 (AZ-1)                                │
│  │  └─ Pod (my-app):                              │
│  │     └─ Container (my-app:latest)               │
│  │                                                │
│  ├─ Node 2 (AZ-1)                                │
│  │  └─ Pod (my-app):                              │
│  │     └─ Container (my-app:latest)               │
│  │                                                │
│  └─ Node 3 (AZ-2)                                │
│     └─ Pod (my-app):                              │
│        └─ Container (my-app:latest)               │
│                                                    │
│  Add-ons:                                          │
│  ├─ VPC CNI (networking)                         │
│  ├─ CoreDNS (service discovery)                  │
│  ├─ Cluster Autoscaler (node scaling)            │
│  ├─ HPA (pod scaling)                            │
│  └─ Prometheus (monitoring)                      │
│                                                    │
└────────────────────────────────────────────────────┘
         ↓
  Services & Ingress
  ├─ Service: Load Balancer / ClusterIP
  └─ Ingress: External HTTP(S) routing
```

### Common Mistakes Beginners Make

1. **Not setting resource requests/limits**: Pods get evicted
2. **Deploying without health checks**: Failed pods aren't restarted
3. **Using latest image tag**: Can't track which version is running
4. **Not using namespaces**: All resources in default namespace is messy
5. **Ignoring RBAC**: Anyone can access everything
6. **Not backing up etcd**: Loss of cluster configuration
7. **Not using ConfigMaps/Secrets**: Hardcoded configs in images

### Interview Questions

1. **What's the difference between ECS and EKS?**
   - ECS: AWS-native, simpler, better AWS integration
   - EKS: Kubernetes standard, portable, larger ecosystem

2. **Explain Kubernetes resource requests and limits.**
   - Requests: Guaranteed minimum resources
   - Limits: Maximum resources pod can use
   - Both important for scheduling and preventing resource starvation

3. **How do you implement CI/CD with EKS?**
   - Push code to GitHub
   - CI pipeline builds image, pushes to ECR
   - CD pipeline updates deployment image
   - kubectl automatically redeploys with new image

4. **What's the difference between Deployment and StatefulSet?**
   - Deployment: Stateless workloads (no persistent identity)
   - StatefulSet: Stateful workloads (databases, persistent storage)

5. **How do you implement multi-tenancy in EKS?**
   - Use namespaces for logical isolation
   - Use RBAC for access control
   - Use resource quotas to limit per-tenant usage
   - Use network policies for network isolation

### Mini Project: Full Kubernetes Application

**Objective**: Deploy complete application stack on EKS

**Requirements**:
- Frontend (React) deployment
- Backend API (Node.js) deployment
- PostgreSQL database (StatefulSet)
- Redis cache (StatefulSet)
- Ingress for external access
- Persistent volumes for databases
- Secrets for credentials
- HPA for auto scaling
- Monitoring with Prometheus/Grafana

**Steps**:
1. Create EKS cluster and node group
2. Create namespaces (frontend, backend, data)
3. Deploy PostgreSQL StatefulSet with persistent storage
4. Deploy Redis StatefulSet
5. Create secrets for database credentials
6. Deploy backend API with environment variables
7. Deploy frontend with backend URL config
8. Create services for each component
9. Create Ingress for external access
10. Set up HPA for backend deployment
11. Install Prometheus/Grafana monitoring
12. Create network policies for security

---

## 12. AWS CodePipeline

### What is CodePipeline?
CodePipeline is AWS's CI/CD orchestration service. It automates the process of building, testing, and deploying code from repository to production.

### Why Use CodePipeline?
**Real-World Example**: A development team has:
- 10 developers pushing code
- Manual testing before deployment
- Manual production deployments
- Frequent human errors

With CodePipeline:
- Automatic build on code push
- Automatic tests before deployment
- Automatic production deployment
- Manual approval gates if needed
- Full audit trail of deployments

**Advantages**:
- Fully managed CI/CD service
- No infrastructure to manage
- Deep AWS integration
- Visual pipeline design
- Multiple deployment targets
- Artifact management

### Key Concepts

**Pipeline Stages**:
```
1. Source (GitHub, CodeCommit)
   └─ Triggered on code push

2. Build (CodeBuild)
   ├─ Compile code
   ├─ Run unit tests
   ├─ Build Docker image
   └─ Push to ECR

3. Deploy (CodeDeploy, CloudFormation, ECS, Lambda)
   ├─ Development environment
   ├─ Staging environment
   └─ Production environment

4. Manual Approval (Optional)
   └─ Human review before production
```

**Artifacts**:
- Output from one stage → input to next stage
- Stored in S3
- Example: Built Docker image, compiled application

### Step-by-Step Setup Guide

#### Step 1: Create CodePipeline IAM Role
```bash
# Create role
aws iam create-role \
  --role-name codepipeline-service-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "codepipeline.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Create policy
cat > pipeline-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:GetObjectVersion"
      ],
      "Resource": "arn:aws:s3:::codepipeline-artifacts/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "codecommit:GetBranch",
        "codecommit:GetCommit",
        "codecommit:UploadArchive",
        "codecommit:CancelUploadArchive"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "codebuild:BatchGetBuilds",
        "codebuild:BatchGetReports",
        "codebuild:BatchGetProjects",
        "codebuild:CreateReport",
        "codebuild:CreateReportGroup",
        "codebuild:UpdateReport",
        "codebuild:StartBuild"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecs:*",
        "codedeploy:*",
        "cloudformation:*",
        "iam:PassRole"
      ],
      "Resource": "*"
    }
  ]
}
EOF

aws iam put-role-policy \
  --role-name codepipeline-service-role \
  --policy-name codepipeline-policy \
  --policy-document file://pipeline-policy.json
```

#### Step 2: Create S3 Bucket for Artifacts
```bash
# Create artifacts bucket
aws s3 mb s3://codepipeline-artifacts-12345 --region us-east-1

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket codepipeline-artifacts-12345 \
  --versioning-configuration Status=Enabled
```

#### Step 3: Create CodeCommit Repository
```bash
# Create repository
aws codecommit create-repository \
  --repository-name my-app \
  --description "My application repository"

# Get clone URL
CLONE_URL=$(aws codecommit get-repository \
  --repository-name my-app \
  --query 'repositoryMetadata.cloneUrlHttp' \
  --output text)

# Clone repository
git clone $CLONE_URL my-app
cd my-app

# Add application code
# Create Dockerfile, buildspec.yml, etc.
```

#### Step 4: Create CodeBuild Project
```bash
# Create service role for CodeBuild
aws iam create-role \
  --role-name codebuild-service-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "codebuild.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Attach necessary policies
aws iam attach-role-policy \
  --role-name codebuild-service-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPowerUser

aws iam put-role-policy \
  --role-name codebuild-service-role \
  --policy-name codebuild-policy \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": ["logs:*", "s3:*"],
      "Resource": "*"
    }]
  }'

# Create CodeBuild project
aws codebuild create-project \
  --name my-app-build \
  --source type=CODECOMMIT,location=https://git-codecommit.us-east-1.amazonaws.com/v1/repos/my-app,gitCloneDepth=1 \
  --artifacts type=CODEPIPELINE \
  --service-role arn:aws:iam::123456789012:role/codebuild-service-role \
  --environment type=LINUX_CONTAINER,image=aws/codebuild/standard:7.0,computeType=BUILD_GENERAL1_SMALL \
  --logs-config cloudWatchLogs={status=ENABLED,groupName=/aws/codebuild/my-app-build}
```

#### Step 5: Create buildspec.yml
```bash
# Create buildspec file in repository
cat > buildspec.yml << 'EOF'
version: 0.2

phases:
  pre_build:
    commands:
      - echo "Logging in to Amazon ECR..."
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
      - REPOSITORY_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/my-app
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}
  
  build:
    commands:
      - echo "Build started on `date`"
      - echo "Building the Docker image..."
      - docker build -t $REPOSITORY_URI:latest .
      - docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
  
  post_build:
    commands:
      - echo "Build completed on `date`"
      - echo "Pushing the Docker images..."
      - docker push $REPOSITORY_URI:latest
      - docker push $REPOSITORY_URI:$IMAGE_TAG
      - echo "Writing image definitions file..."
      - printf '[{"name":"my-app","imageUri":"%s"}]' $REPOSITORY_URI:$IMAGE_TAG > imagedefinitions.json

artifacts:
  files: imagedefinitions.json
  name: BuildArtifact

cache:
  paths:
    - '/root/.docker/**/*'
EOF

git add buildspec.yml
git commit -m "Add buildspec for CodeBuild"
git push
```

#### Step 6: Create CodePipeline
```bash
# Create pipeline definition
cat > pipeline.json << 'EOF'
{
  "pipeline": {
    "name": "my-app-pipeline",
    "roleArn": "arn:aws:iam::123456789012:role/codepipeline-service-role",
    "artifactStore": {
      "type": "S3",
      "location": "codepipeline-artifacts-12345"
    },
    "stages": [
      {
        "name": "Source",
        "actions": [
          {
            "name": "SourceAction",
            "actionTypeId": {
              "category": "Source",
              "owner": "AWS",
              "provider": "CodeCommit",
              "version": "1"
            },
            "configuration": {
              "RepositoryName": "my-app",
              "BranchName": "main",
              "PollForSourceChanges": "false"
            },
            "outputArtifacts": [
              {"name": "SourceOutput"}
            ]
          }
        ]
      },
      {
        "name": "Build",
        "actions": [
          {
            "name": "BuildAction",
            "actionTypeId": {
              "category": "Build",
              "owner": "AWS",
              "provider": "CodeBuild",
              "version": "1"
            },
            "configuration": {
              "ProjectName": "my-app-build"
            },
            "inputArtifacts": [
              {"name": "SourceOutput"}
            ],
            "outputArtifacts": [
              {"name": "BuildOutput"}
            ]
          }
        ]
      },
      {
        "name": "Deploy-Dev",
        "actions": [
          {
            "name": "DeployToECS-Dev",
            "actionTypeId": {
              "category": "Deploy",
              "owner": "AWS",
              "provider": "ECS",
              "version": "1"
            },
            "configuration": {
              "ClusterName": "dev-cluster",
              "ServiceName": "my-app-service",
              "FileName": "imagedefinitions.json"
            },
            "inputArtifacts": [
              {"name": "BuildOutput"}
            ]
          }
        ]
      },
      {
        "name": "Approval",
        "actions": [
          {
            "name": "ManualApproval",
            "actionTypeId": {
              "category": "Approval",
              "owner": "AWS",
              "provider": "Manual",
              "version": "1"
            },
            "configuration": {
              "CustomData": "Please review dev deployment before proceeding to production"
            }
          }
        ]
      },
      {
        "name": "Deploy-Prod",
        "actions": [
          {
            "name": "DeployToECS-Prod",
            "actionTypeId": {
              "category": "Deploy",
              "owner": "AWS",
              "provider": "ECS",
              "version": "1"
            },
            "configuration": {
              "ClusterName": "prod-cluster",
              "ServiceName": "my-app-service",
              "FileName": "imagedefinitions.json"
            },
            "inputArtifacts": [
              {"name": "BuildOutput"}
            ]
          }
        ]
      }
    ]
  }
}
EOF

# Create the pipeline
aws codepipeline create-pipeline --cli-input-json file://pipeline.json
```

#### Step 7: Enable Automatic Triggering
```bash
# Create EventBridge rule for CodeCommit push
aws events put-rule \
  --name codecommit-push \
  --event-pattern '{
    "detail-event": ["referenceCreated", "referenceUpdated"],
    "event": ["codecommit"],
    "detail": {"event": ["referenceCreated", "referenceUpdated"], "repositoryName": ["my-app"], "referenceType": ["branch"], "referenceName": ["main"]}
  }'

# Add CodePipeline as target
aws events put-targets \
  --rule codecommit-push \
  --targets "Id"="1","Arn"="arn:aws:codepipeline:us-east-1:123456789012:my-app-pipeline","RoleArn"="arn:aws:iam::123456789012:role/eventbridge-codepipeline-role"
```

### Important Commands

```bash
# List pipelines
aws codepipeline list-pipelines

# Get pipeline details
aws codepipeline get-pipeline --name my-app-pipeline

# Get pipeline execution history
aws codepipeline list-pipeline-executions --pipeline-name my-app-pipeline

# Get details of specific execution
aws codepipeline get-pipeline-execution \
  --pipeline-name my-app-pipeline \
  --pipeline-execution-id <execution-id>

# Start pipeline execution manually
aws codepipeline start-pipeline-execution --pipeline-name my-app-pipeline

# Put approval result
aws codepipeline put-approval-result \
  --pipeline-name my-app-pipeline \
  --stage-name Approval \
  --action-name ManualApproval \
  --result summary="Approved for production",status=Approved

# Get CodeBuild logs
aws codebuild batch-get-build-logs --ids <build-id>

# List CodeBuild projects
aws codebuild list-projects

# Delete pipeline
aws codepipeline delete-pipeline --name my-app-pipeline
```

### Architecture Diagram

```
┌──────────────────────────────────────────────────────┐
│            CodePipeline: my-app-pipeline             │
├──────────────────────────────────────────────────────┤
│                                                      │
│ Stage 1: Source                                      │
│ ├─ CodeCommit: my-app repo (main branch)             │
│ └─ Triggered on code push (EventBridge)              │
│        │                                              │
│        ↓                                              │
│ Stage 2: Build                                       │
│ ├─ CodeBuild: my-app-build project                  │
│ │  ├─ Build Docker image                            │
│ │  ├─ Run tests                                      │
│ │  └─ Push to ECR                                    │
│ └─ Output: imagedefinitions.json (S3 artifact)       │
│        │                                              │
│        ↓                                              │
│ Stage 3: Deploy-Dev                                  │
│ ├─ CodeDeploy: Deploy to dev-cluster                │
│ └─ Update ECS service with new image                │
│        │                                              │
│        ↓                                              │
│ Stage 4: Approval                                    │
│ └─ Manual approval (SNS notification)                │
│        │                                              │
│        ↓                                              │
│ Stage 5: Deploy-Prod                                 │
│ ├─ CodeDeploy: Deploy to prod-cluster               │
│ └─ Update ECS service with new image                │
│                                                      │
│ Artifact Store: S3 (codepipeline-artifacts)         │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### Common Mistakes Beginners Make

1. **Not setting permissions correctly**: Pipeline fails with permission errors
2. **buildspec.yml in wrong location**: Must be in repository root
3. **Not storing secrets securely**: Use Secrets Manager, not hardcoded
4. **Manual approval notifications not configured**: Approvers don't know to approve
5. **No rollback strategy**: Can't quickly revert bad deployments
6. **Not testing pipeline**: First deployment to prod usually fails
7. **Artifact retention too high**: Wastes S3 storage

### Interview Questions

1. **Explain the typical CI/CD pipeline flow.**
   - Source: Code push triggers pipeline
   - Build: Compile, test, build artifacts
   - Test: Run integration tests
   - Deploy Dev: Deploy to development
   - Approval: Manual review
   - Deploy Prod: Deploy to production

2. **How do you implement canary deployments in CodePipeline?**
   - CodeDeploy with traffic shifting
   - Deploy to small percentage of traffic first
   - Monitor metrics for errors
   - Automatically rollback if issues detected

3. **How do you manage secrets in CI/CD?**
   - Use AWS Secrets Manager
   - Pass secrets as environment variables to CodeBuild
   - Never commit secrets to repository
   - Use IAM roles for service authentication

4. **What's the difference between CodePipeline, CodeBuild, and CodeDeploy?**
   - CodePipeline: Orchestrates the overall CI/CD workflow
   - CodeBuild: Compiles code and runs tests
   - CodeDeploy: Deploys code to target environments

5. **How do you handle pipeline failures?**
   - CloudWatch alarms for pipeline failures
   - SNS notifications to team
   - Automatic rollback to previous version
   - Manual intervention with approval gates

### Mini Project: Complete CI/CD Pipeline

**Objective**: Build and deploy a web application through complete pipeline

**Requirements**:
- CodeCommit repository
- CodeBuild project for building Docker image
- Three deployment stages (Dev, Staging, Prod)
- Manual approval before production
- Automated testing in build stage
- Rollback capability
- Pipeline notifications via SNS

**Steps**:
1. Create CodeCommit repository
2. Add application code with tests
3. Create buildspec.yml with:
   - Unit tests
   - Docker image build
   - Push to ECR
4. Create CodeBuild project
5. Create three ECS services (dev, staging, prod)
6. Create CodePipeline with stages:
   - Source → CodeCommit
   - Build → CodeBuild
   - Deploy-Dev → ECS
   - Deploy-Staging → ECS
   - Approval → Manual
   - Deploy-Prod → ECS
7. Set up SNS for notifications
8. Configure automatic triggering
9. Test pipeline with code push
10. Verify deployments in each environment

---

## Best Practices

### Security Best Practices

1. **Principle of Least Privilege**
   - Users/roles should have minimum permissions
   - Use resource-level permissions when possible
   - Regularly audit and remove unused permissions

2. **Encryption**
   - Encrypt data at rest (S3, RDS, EBS)
   - Encrypt data in transit (TLS/SSL)
   - Use KMS for key management

3. **Access Control**
   - Use IAM roles (not access keys) for services
   - Enable MFA for sensitive operations
   - Use temporary credentials (assume role)

4. **Network Security**
   - Use VPC with private subnets for databases
   - Implement security groups and NACLs
   - Use VPN/Direct Connect for on-premises access

5. **Monitoring & Logging**
   - Enable CloudTrail for API logging
   - Monitor CloudWatch for suspicious activity
   - Set up alerts for security events

### Performance Best Practices

1. **Caching**
   - Use ElastiCache for frequently accessed data
   - CloudFront for static content
   - Application-level caching

2. **Database Optimization**
   - Use read replicas for read-heavy workloads
   - Implement proper indexing
   - Use connection pooling

3. **Scalability**
   - Use Auto Scaling for elastic capacity
   - Implement load balancing
   - Design stateless applications

4. **Monitoring**
   - Monitor key metrics (CPU, memory, latency)
   - Set up alarms for threshold violations
   - Use X-Ray for distributed tracing

### Cost Optimization

1. **Right-Sizing**
   - Choose appropriate instance types
   - Use reserved instances for baseline load
   - Spot instances for non-critical workloads

2. **Storage Optimization**
   - Use S3 Glacier for archival data
   - Enable S3 lifecycle policies
   - Delete unused snapshots and volumes

3. **Data Transfer**
   - Use CloudFront to reduce data transfer costs
   - Consolidate services in same region
   - Monitor data transfer charges

---

## DevOps Career Tips

### Skills to Develop

1. **Cloud Platforms**: AWS, Azure, GCP
2. **Infrastructure as Code**: Terraform, CloudFormation
3. **Containerization**: Docker, Kubernetes
4. **CI/CD**: Jenkins, GitLab CI, GitHub Actions
5. **Monitoring**: Prometheus, ELK Stack, DataDog
6. **Scripting**: Python, Bash, Go
7. **Databases**: SQL, NoSQL, database optimization
8. **Networking**: TCP/IP, DNS, firewalls, VPN

### Career Path

**Junior DevOps Engineer** (0-2 years):
- Deploy and maintain applications
- Troubleshoot infrastructure issues
- Document processes and runbooks
- Learn AWS services and best practices

**Mid-Level DevOps Engineer** (2-5 years):
- Design scalable architectures
- Implement CI/CD pipelines
- Optimize costs and performance
- Lead small infrastructure projects
- Mentor junior team members

**Senior DevOps Engineer** (5+ years):
- Design enterprise architectures
- Lead infrastructure transformations
- Implement advanced automation
- Define DevOps strategy
- Mentor team and establish best practices

### Learning Resources

- AWS Documentation: https://docs.aws.amazon.com
- AWS Training: https://aws.amazon.com/training
- Linux Academy / A Cloud Guru: Online courses
- Terraform Registry: https://registry.terraform.io
- Kubernetes Documentation: https://kubernetes.io/docs
- Medium/Dev.to: Technical articles
- YouTube: Tutorial videos and demonstrations

### Certifications

- **AWS Solutions Architect Associate**: Foundation, popular
- **AWS Developer Associate**: Application development focused
- **AWS SysOps Administrator**: Operations focused
- **AWS Solutions Architect Professional**: Advanced
- **AWS DevOps Engineer Professional**: Specialized

---

## Final Deployment Mini-Project

### Project: Deploy a Scalable E-Commerce Platform

This comprehensive project combines multiple AWS services to create a production-ready e-commerce platform.

### Architecture Overview

```
┌────────────────────────────────────────────────────────┐
│            CloudFront (CDN)                            │
│         (Cache static content globally)                │
└────────────┬────────────────────────────────────────────┘
             │
┌────────────┴────────────────────────────────────────────┐
│           Application Load Balancer (HTTPS)            │
│         (Distribute traffic, SSL termination)           │
└────────────┬────────────────────────────────────────────┘
             │
    ┌────────┴─────────┐
    ↓                  ↓
┌─────────────────────────────────────────────────────┐
│        ECS Cluster (Container Orchestration)        │
├─────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐               │
│  │ Frontend     │  │ Backend API  │               │
│  │ Service      │  │ Service      │               │
│  │ (3+ tasks)   │  │ (3+ tasks)   │               │
│  └──────────────┘  └──────────────┘               │
└─────────────────────────────────────────────────────┘
             │
    ┌────────┴─────────────────┬──────────────┐
    ↓                          ↓              ↓
┌──────────────┐      ┌──────────────┐  ┌────────┐
│ RDS Aurora   │      │ ElastiCache  │  │   S3   │
│ (Database)   │      │  (Sessions)  │  │Products│
│ Multi-AZ     │      │   & Caching  │  │ Images │
└──────────────┘      └──────────────┘  └────────┘
    │
    └─────────────────────────────────┐
                                      ↓
┌─────────────────────────────────────────────────┐
│     AWS CodePipeline (CI/CD)                    │
│ ┌──────────────────────────────────────────┐   │
│ │ GitHub → Build → Test → Deploy-Staging  │   │
│ │        → Approval → Deploy-Production    │   │
│ └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘

Monitoring & Logging:
├─ CloudWatch (Metrics, Logs, Alarms)
├─ X-Ray (Distributed Tracing)
└─ CloudTrail (Audit Logging)
```

### Implementation Steps

#### Phase 1: Infrastructure Setup (Week 1)

1. **VPC and Networking**
   ```bash
   # Create VPC with 6 subnets across 3 AZs
   # Configure Internet Gateway and NAT Gateway
   # Create security groups for each tier
   ```

2. **IAM Roles and Permissions**
   ```bash
   # Create roles for:
   # - ECS task execution
   # - ECS task (app permissions)
   # - CodePipeline
   # - CodeBuild
   # - Lambda (if using serverless)
   ```

3. **RDS Database**
   ```bash
   # Create Aurora PostgreSQL cluster
   # Multi-AZ for high availability
   # Enable automated backups
   # Configure security groups
   ```

4. **ElastiCache**
   ```bash
   # Create Redis cluster
   # Multi-node for high availability
   # Enable automatic failover
   ```

5. **S3 Buckets**
   ```bash
   # Create buckets for:
   # - Product images (with CloudFront)
   # - Application logs
   # - Backups
   # - CodePipeline artifacts
   ```

#### Phase 2: Application Containerization (Week 2)

1. **Frontend Application**
   ```dockerfile
   # Dockerfile for React frontend
   FROM node:18-alpine
   WORKDIR /app
   COPY package*.json ./
   RUN npm install
   COPY . .
   RUN npm run build
   
   FROM nginx:alpine
   COPY --from=0 /app/build /usr/share/nginx/html
   EXPOSE 80
   ```

2. **Backend API**
   ```dockerfile
   # Dockerfile for Node.js API
   FROM node:18-alpine
   WORKDIR /app
   COPY package*.json ./
   RUN npm install
   COPY . .
   EXPOSE 5000
   CMD ["node", "server.js"]
   ```

3. **Push to ECR**
   ```bash
   # Create ECR repositories
   # Build and push images
   ```

#### Phase 3: ECS Deployment (Week 3)

1. **ECS Cluster**
   ```bash
   # Create cluster with Fargate launch type
   ```

2. **Task Definitions**
   ```bash
   # Frontend: 256 CPU, 512 MB memory
   # Backend: 512 CPU, 1024 MB memory
   # Include health checks
   # Configure CloudWatch logging
   ```

3. **Services**
   ```bash
   # Frontend service (replicas: 3)
   # Backend service (replicas: 3+)
   # Attach to load balancer
   ```

#### Phase 4: Load Balancing & Scaling (Week 4)

1. **Application Load Balancer**
   ```bash
   # Create ALB across 2+ AZs
   # Configure listeners:
   #   - HTTP (port 80) → redirect to HTTPS
   #   - HTTPS (port 443) → both services
   # Path-based routing:
   #   - / → Frontend
   #   - /api/* → Backend
   ```

2. **Auto Scaling**
   ```bash
   # Frontend: Scale based on request count
   # Backend: Scale based on CPU utilization
   # Min: 2, Max: 10 replicas
   ```

3. **CloudFront**
   ```bash
   # Create distribution for:
   #   - S3 product images
   #   - Static assets from frontend
   # Set cache policies
   # Enable compression
   ```

#### Phase 5: CI/CD Pipeline (Week 5)

1. **CodeCommit Repository**
   ```bash
   # Create repo with main, develop branches
   # Protect main branch with pull requests
   ```

2. **CodeBuild**
   ```bash
   # Build project with buildspec.yml:
   #   - Run unit tests
   #   - Build Docker images
   #   - Push to ECR
   #   - Update image definitions
   ```

3. **CodePipeline**
   ```bash
   # Stages:
   #   1. Source (CodeCommit)
   #   2. Build (CodeBuild)
   #   3. Deploy-Staging (ECS)
   #   4. Approval (Manual)
   #   5. Deploy-Production (ECS)
   ```

#### Phase 6: Monitoring & Logging (Week 6)

1. **CloudWatch**
   ```bash
   # Create log groups for:
   #   - Frontend (/ecs/frontend)
   #   - Backend API (/ecs/backend)
   #   - RDS (enhanced monitoring)
   
   # Create alarms for:
   #   - High CPU utilization
   #   - High memory usage
   #   - Unhealthy targets
   #   - Error rate spikes
   #   - RDS connections
   ```

2. **X-Ray**
   ```bash
   # Enable X-Ray tracing
   # Trace requests end-to-end
   # Identify bottlenecks
   ```

3. **Dashboard**
   ```bash
   # Create CloudWatch dashboard
   # Show:
   #   - Request count
   #   - Response time (p50, p99)
   #   - Error rate
   #   - Resource utilization
   #   - Active connections
   ```

#### Phase 7: Security Hardening (Week 7)

1. **Network Security**
   ```bash
   # Configure security groups:
   #   - ALB: Allow 80, 443 from 0.0.0.0/0
   #   - ECS: Allow ports from ALB only
   #   - RDS: Allow MySQL from ECS only
   #   - ElastiCache: Allow Redis from ECS only
   ```

2. **Data Encryption**
   ```bash
   # Enable encryption at rest:
   #   - RDS: KMS encryption
   #   - S3: SSE-S3 or SSE-KMS
   #   - ElastiCache: At-rest encryption
   #   - EBS: Default encryption
   
   # Encryption in transit:
   #   - ALB: HTTPS/TLS
   #   - RDS: SSL connections
   #   - ElastiCache: TLS
   ```

3. **Secrets Management**
   ```bash
   # Store in Secrets Manager:
   #   - Database password
   #   - API keys
   #   - OAuth tokens
   #   - JWTs signing keys
   ```

#### Phase 8: Performance Optimization (Week 8)

1. **Database Optimization**
   ```bash
   # Create read replicas for:
   #   - Product catalog queries
   #   - User profile reads
   #   - Analytics queries
   ```

2. **Caching Strategy**
   ```bash
   # Cache with ElastiCache:
   #   - Product catalog
   #   - User sessions
   #   - API responses
   #   - Database query results
   ```

3. **CDN Optimization**
   ```bash
   # CloudFront:
   #   - Cache product images
   #   - Cache JavaScript/CSS bundles
   #   - Set appropriate TTLs
   #   - Enable compression
   ```

### Testing Checklist

- [ ] Deploy code to staging via pipeline
- [ ] Test all user workflows
- [ ] Load test with 1000+ concurrent users
- [ ] Test database failover
- [ ] Test RDS read replicas
- [ ] Test cache invalidation
- [ ] Test auto scaling (simulate high load)
- [ ] Test recovery from failures
- [ ] Verify all logs are being collected
- [ ] Check CloudWatch dashboards
- [ ] Test monitoring alarms
- [ ] Verify HTTPS/TLS works
- [ ] Test disaster recovery procedures
- [ ] Verify backups can be restored
- [ ] Check compliance and audit logs

### Production Readiness Checklist

- [ ] Automated CI/CD pipeline fully functional
- [ ] Manual approval gates before production
- [ ] Rollback procedures tested and documented
- [ ] All secrets stored in Secrets Manager
- [ ] CloudTrail enabled for audit logging
- [ ] CloudWatch alarms configured
- [ ] PagerDuty/Slack integration for alerts
- [ ] Database automated backups configured
- [ ] Disaster recovery plan documented
- [ ] Load testing shows capacity limits
- [ ] Security audit completed
- [ ] Documentation updated
- [ ] Team trained on deployment process
- [ ] Incident response plan in place
- [ ] Cost optimization review completed

### Estimated Costs (Monthly)

```
EC2/ECS (Fargate):        $500
RDS Aurora:              $1,200
ElastiCache Redis:        $150
S3 & Data Transfer:       $200
CloudFront:              $100
Load Balancer:            $20
Misc (CloudWatch, etc):   $50
                         -----
Total:                  ~$2,220/month

Recommendations for cost optimization:
- Use reserved instances for baseline
- Implement lifecycle policies for S3
- Use spot instances for non-critical tasks
- Monitor unused resources
- Right-size instance types
```

---

## Conclusion

This comprehensive guide has covered 12 essential AWS services, from foundational compute (EC2) to advanced orchestration (EKS) and automation (CodePipeline). Key takeaways:

1. **Start Simple**: Begin with EC2, S3, and IAM before moving to complex services
2. **Plan Architecture**: Design for scalability, availability, and security from the start
3. **Automate Everything**: Use Infrastructure as Code, CI/CD, and monitoring
4. **Monitor Continuously**: Implement CloudWatch, X-Ray, and alerting from day one
5. **Security First**: Apply least privilege, encryption, and network isolation
6. **Optimize Costs**: Regular reviews and right-sizing prevent bill shocks
7. **Document & Train**: Ensure team knowledge transfer and process documentation

The final mini-project demonstrates how these services work together in a real-world scenario. Continue learning, practicing, and staying updated with new AWS features to advance your DevOps career.

---

## Additional Resources

- AWS Free Tier: https://aws.amazon.com/free
- AWS Whitepapers: https://aws.amazon.com/whitepapers
- AWS Workshops: https://workshops.aws
- AWS User Groups: Local meetups and communities
- Terraform AWS Provider: https://registry.terraform.io/providers/hashicorp/aws
- AWS SAM (Serverless Application Model): For serverless development

Good luck on your AWS DevOps journey! 🚀
