# AWS on Ubuntu — Learning Setup Guide

A practical README for setting up and learning AWS (Amazon Web Services) from an Ubuntu machine. Covers CLI installation, account setup, the deep-dive lesson template used for every service, and per-service lessons (starting with IAM).

---

## Table of Contents
1. [Prerequisites](#1-prerequisites)
2. [Create an AWS Account](#2-create-an-aws-account)
3. [Install AWS CLI on Ubuntu](#3-install-aws-cli-on-ubuntu)
4. [Configure AWS CLI Credentials](#4-configure-aws-cli-credentials)
5. [Core AWS Services to Learn](#5-core-aws-services-to-learn)
6. [Hands-on Learning Path](#6-hands-on-learning-path)
7. [Useful CLI Commands](#7-useful-cli-commands)
8. [Cost Control & Free Tier Safety](#8-cost-control--free-tier-safety)
9. [Recommended Learning Resources](#9-recommended-learning-resources)
10. [Cleanup Checklist](#10-cleanup-checklist)
11. [Service Lesson Template](#11-service-lesson-template)
12. [Progress Tracker](#12-progress-tracker)
13. [Service 01 — IAM](#13-service-01--iam)

---

## 1. Prerequisites

- Ubuntu 20.04 / 22.04 / 24.04 (or WSL2 Ubuntu on Windows)
- A valid email address and phone number (needed for AWS account verification)
- A debit/credit card (required by AWS even for Free Tier usage — used for identity verification)
- Basic terminal familiarity (`cd`, `sudo`, `apt`)

Update your system first:
```bash
sudo apt update && sudo apt upgrade -y
```

---

## 2. Create an AWS Account

1. Go to https://aws.amazon.com and click **Create an AWS Account**.
2. Verify your email and phone number.
3. Enter payment details (required, but Free Tier services won't charge you if you stay within limits).
4. Choose the **Basic Support Plan** (Free).
5. Once logged in, go to the **IAM** console and create an **admin IAM user** instead of using the root account for daily work (best practice).

> ⚠️ Never use your root account for regular tasks. Root should only be used for account-level actions (billing, closing account, etc.).

---

## 3. Install AWS CLI on Ubuntu

### Option A — Official installer (recommended, always latest v2)
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip -y
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

### Option B — via apt (may be outdated)
```bash
sudo apt install awscli -y
```

### Optional: Install additional tooling
```bash
# AWS SAM CLI (for serverless projects)
pip install aws-sam-cli --break-system-packages

# eksctl (for EKS/Kubernetes)
curl --silent --location "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin

# Terraform (Infrastructure as Code)
sudo apt install -y gnupg software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform -y
```

---

## 4. Configure AWS CLI Credentials

1. In the IAM console, create an **Access Key** for your IAM admin user (IAM → Users → Security credentials → Create access key).
2. Run:
```bash
aws configure
```
3. Enter when prompted:
   - **AWS Access Key ID**
   - **AWS Secret Access Key**
   - **Default region** (e.g. `ap-south-1` for Mumbai)
   - **Default output format** (`json` recommended)

4. Verify it works:
```bash
aws sts get-caller-identity
```

> 🔒 Never commit your Access Key/Secret to GitHub or share it publicly. Rotate keys periodically and delete unused ones.

---

## 5. Core AWS Services to Learn

| Category | Service | Why Learn It |
|---|---|---|
| **Identity & Access** | **IAM** | Manage users, roles, permissions — foundation of AWS security |
| **Compute** | **EC2** | Virtual servers; core compute building block |
| **Compute** | **Lambda** | Serverless functions; event-driven compute |
| **Storage** | **S3** | Object storage for files, static websites, backups |
| **Storage** | **EBS** | Block storage attached to EC2 instances |
| **Networking** | **VPC** | Virtual private network — subnets, route tables, security groups |
| **Networking** | **Route 53** | DNS management and domain routing |
| **Database** | **RDS** | Managed relational databases (MySQL, PostgreSQL, etc.) |
| **Database** | **DynamoDB** | Managed NoSQL database |
| **Monitoring** | **CloudWatch** | Logs, metrics, alarms |
| **Deployment** | **CloudFormation** | Infrastructure as Code (native AWS) |
| **Containers** | **ECS / EKS** | Docker container orchestration |
| **CDN** | **CloudFront** | Content delivery network |
| **Messaging** | **SNS / SQS** | Notifications and queuing for decoupled architectures |
| **Billing** | **Cost Explorer / Budgets** | Track and control spending |

**Suggested learning order:** IAM → EC2 → S3 → VPC → RDS → CloudWatch → Lambda → CloudFormation → Containers (ECS/EKS)

---

## 6. Hands-on Learning Path

### Beginner Projects
- Launch an EC2 instance, SSH into it from Ubuntu, host a simple web server (Nginx/Apache).
- Create an S3 bucket, upload files, host a static website.
- Create an IAM user/group/policy and test permission boundaries.

### Intermediate Projects
- Set up a custom VPC with public/private subnets and a bastion host.
- Deploy a Lambda function triggered by an S3 upload event.
- Launch an RDS MySQL/PostgreSQL instance and connect from an EC2 app.
- Set CloudWatch alarms for CPU usage and billing.

### Advanced Projects
- Write CloudFormation or Terraform templates to provision your VPC + EC2 + RDS stack automatically.
- Deploy a containerized app on ECS Fargate.
- Build a serverless REST API using API Gateway + Lambda + DynamoDB.

---

## 7. Useful CLI Commands

```bash
# List EC2 instances
aws ec2 describe-instances

# List S3 buckets
aws s3 ls

# Create an S3 bucket
aws s3 mb s3://your-unique-bucket-name

# Upload a file to S3
aws s3 cp myfile.txt s3://your-unique-bucket-name/

# List IAM users
aws iam list-users

# Check current billing/cost (requires Cost Explorer enabled)
aws ce get-cost-and-usage --time-period Start=2026-06-01,End=2026-07-01 --granularity MONTHLY --metrics "BlendedCost"

# Stop/terminate an EC2 instance (avoid surprise charges)
aws ec2 stop-instances --instance-ids i-xxxxxxxxxxxxxxxxx
aws ec2 terminate-instances --instance-ids i-xxxxxxxxxxxxxxxxx
```

---

## 8. Cost Control & Free Tier Safety

- Enable **AWS Budgets** and set a $1–5 alert threshold immediately after account creation.
- Use only **Free Tier eligible** resources while learning (e.g. `t2.micro` / `t3.micro` EC2, 5GB S3 standard storage).
- Always **stop or terminate** EC2 instances, RDS databases, and NAT Gateways when not in use — these are the most common sources of unexpected bills.
- Delete unused Elastic IPs — AWS charges for unattached ones.
- Review the **Billing Dashboard** weekly while learning.

---

## 9. Recommended Learning Resources

- AWS official docs: https://docs.aws.amazon.com
- AWS Free Tier details: https://aws.amazon.com/free
- AWS Skill Builder (free courses): https://skillbuilder.aws
- AWS Certified Cloud Practitioner (great starting certification)

---

## 10. Cleanup Checklist

Before ending a learning session, verify:
- [ ] All EC2 instances stopped/terminated
- [ ] Unused S3 buckets/objects deleted
- [ ] RDS instances stopped/deleted
- [ ] Elastic IPs released
- [ ] NAT Gateways deleted (they bill hourly even when idle)
- [ ] CloudWatch alarms reviewed
- [ ] Billing dashboard checked for surprise charges

---

*This guide is meant as a personal learning reference — adapt regions, instance types, and services to your specific coursework or project goals.*

---

## 11. Service Lesson Template

Every service in this README (starting with IAM below) is taught using this fixed 11-part structure, so lessons stay consistent and comparable as the list grows:

1. **What is this service?** — problem it solves, why it exists, when to use / not use it
2. **Where is it in AWS?** — Console path, CLI commands, terminal commands, SDK example
3. **Prerequisites** — dependent services, required IAM permissions/roles, networking needs
4. **How to Create It** — Console method (every option explained) + CLI method (every flag explained, with expected output and common errors)
5. **How to Access It** — real connection methods (SSH, DB clients, kubectl, invoke, etc.)
6. **How It Connects to Other AWS Services** — dependency diagram + reasoning
7. **Terminal Workflow** — full real-world setup using only terminal commands, in order
8. **Verification** — commands to confirm each step worked, with output explained
9. **Troubleshooting** — common errors, causes, fixes, debugging commands, log locations
10. **Real-World Workflow** — how production teams actually use the service end-to-end
11. **Mini Lab** — a hands-on terminal-only exercise to complete before moving to the next service

**Learning order used in this README:** IAM → EC2 → S3 → VPC → RDS → CloudWatch → Lambda → CloudFormation → ECS → EKS

---

## 12. Progress Tracker

| # | Service | Status |
|---|---|---|
| 01 | **IAM** | ✅ Lesson complete — see [Section 13](#13-service-01--iam) |
| 02 | EC2 | ⏳ Not started |
| 03 | S3 | ⏳ Not started |
| 04 | VPC | ⏳ Not started |
| 05 | RDS | ⏳ Not started |
| 06 | CloudWatch | ⏳ Not started |
| 07 | Lambda | ⏳ Not started |
| 08 | CloudFormation | ⏳ Not started |
| 09 | ECS | ⏳ Not started |
| 10 | EKS | ⏳ Not started |

> Rule: don't move to the next service until the Mini Lab for the current one is completed and understanding is confirmed. This tracker updates as each lesson finishes.

---

## 13. Service 01 — IAM

### 13.1 What is this service?

**What problem does it solve?**
Cloud resources need to be locked down — you can't let every request act as an all-powerful root account. IAM solves the problem of "who can do what, on which resource" across your entire AWS account.

**Why was it created?**
AWS needed a way to grant fine-grained, auditable access to humans, applications, and other AWS services without sharing root credentials. Before IAM, everyone would share one root login — a massive security risk.

**When should you use it?**
- Always. Every AWS account uses IAM whether you interact with it directly or not.
- Specifically: creating individual users for team members, creating roles for EC2/Lambda/ECS to access other services, restricting what a CI/CD pipeline can touch, enforcing MFA.

**When should you NOT use it (directly)?**
- You rarely create IAM users for *applications* — use IAM **Roles** instead (temporary credentials, no long-lived keys to leak).
- Don't over-engineer permissions early in learning — start with a scoped admin user, refine later.

### 13.2 Where is it in AWS?

**Console path:**
`AWS Console → search "IAM" → IAM Dashboard`
- Users: `IAM → Users`
- Roles: `IAM → Roles`
- Policies: `IAM → Policies`
- Groups: `IAM → User groups`

**CLI:**
```bash
aws iam list-users
aws iam list-roles
aws iam list-policies --scope Local
aws iam get-user
```

**Linux terminal (setup, not IAM-specific):**
```bash
aws configure                  # sets up credentials used by every IAM-authenticated call
aws sts get-caller-identity    # confirms WHO you're authenticated as
```

**SDK example (Python boto3):**
```python
import boto3
iam = boto3.client('iam')
response = iam.list_users()
print(response['Users'])
```

### 13.3 Prerequisites

IAM is the **foundation service** — it has no dependencies. It requires:
- Just an AWS account (root or another IAM user with `iam:*` permissions to manage it).
- No VPC, no Security Group, no other service needed.

To create IAM users/roles/policies, the identity doing the creating needs:
- `iam:CreateUser`, `iam:CreateRole`, `iam:CreatePolicy`, `iam:AttachUserPolicy`, etc. (usually bundled in `IAMFullAccess` or `AdministratorAccess` while learning).

### 13.4 How to Create It

#### Method 1 — AWS Console

**Create an IAM user:**
1. `IAM → Users → Create user`
2. Enter a username (e.g. `devops-learner`)
3. "Provide user access to the AWS Management Console" — check this if the person needs to log in via browser; leave unchecked if it's purely for CLI/API access.
4. Set permissions:
   - **Attach policies directly** → search and select e.g. `AdministratorAccess` (learning only — restrict later)
   - Or **Add user to group** (recommended long-term pattern)
5. Review → Create user
6. On the confirmation page, download the `.csv` with credentials (console password) — this is shown **only once**.

**Create an Access Key (for CLI use):**
1. `IAM → Users → [your user] → Security credentials tab`
2. `Create access key`
3. Choose use case: "Command Line Interface (CLI)"
4. Acknowledge the recommendation and confirm
5. Copy the **Access Key ID** and **Secret Access Key** immediately — the secret is shown only once.

**Create a Role (for services, not people):**
1. `IAM → Roles → Create role`
2. Trusted entity type: **AWS service** (e.g. EC2, Lambda)
3. Use case: select the specific service (e.g. `EC2`)
4. Attach permission policies (e.g. `AmazonS3ReadOnlyAccess` if this EC2 needs to read S3)
5. Name the role (e.g. `EC2-S3-ReadOnly-Role`) → Create

#### Method 2 — AWS CLI

```bash
# Create a user
aws iam create-user --user-name devops-learner
```
- `--user-name`: the IAM identity name, must be unique in the account.
- **Output:** JSON with a `User` object containing `UserId`, `Arn`, `CreateDate`.

```bash
# Attach a managed policy to the user
aws iam attach-user-policy \
  --user-name devops-learner \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```
- `--policy-arn`: full ARN of an AWS-managed or customer-managed policy.
- No output on success (empty response = success in IAM CLI calls).

```bash
# Create an access key for CLI/programmatic use
aws iam create-access-key --user-name devops-learner
```
- **Output:** `AccessKeyId` and `SecretAccessKey` — save immediately, the secret is never retrievable again.

```bash
# Create a role with a trust policy (trust-policy.json defines WHO can assume it)
cat > trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "ec2.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}
EOF

aws iam create-role \
  --role-name EC2-S3-ReadOnly-Role \
  --assume-role-policy-document file://trust-policy.json
```
- `--assume-role-policy-document`: defines *who/what* can assume this role (here, EC2 instances).
- `file://` prefix tells the CLI to read from a local file.

```bash
# Attach a permission policy to the role
aws iam attach-role-policy \
  --role-name EC2-S3-ReadOnly-Role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

**Common errors:**

| Error | Cause | Fix |
|---|---|---|
| `EntityAlreadyExists` | Username/role already exists | Choose a different name or delete the old one |
| `AccessDenied` | Your current credentials lack IAM permissions | Use an admin user, or request permission |
| `MalformedPolicyDocument` | Bad JSON in trust/permission policy | Validate JSON syntax (`jq . trust-policy.json`) |

### 13.5 How to Access It

IAM itself isn't something you "SSH into" — you access it by **authenticating as an IAM identity**.

```bash
# Verify who you're currently authenticated as
aws sts get-caller-identity
```
Output shows `Account`, `UserId`, and `Arn` — confirms your active identity.

```bash
# Switch to using a specific named profile (if multiple IAM users are configured)
aws configure --profile devops-learner
aws s3 ls --profile devops-learner
```

```bash
# Assume a role temporarily (common for cross-account or elevated access)
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/EC2-S3-ReadOnly-Role \
  --role-session-name test-session
```
This returns temporary credentials (`AccessKeyId`, `SecretAccessKey`, `SessionToken`) valid for a limited time — used internally by services like EC2/Lambda automatically, no manual key management needed.

### 13.6 How It Connects to Other AWS Services

```
IAM (Users, Roles, Policies)
   ↓ grants permissions to
EC2 Instance (via Instance Profile / Role)
   ↓ allows EC2 to call
S3 (upload backups, read config files)
   ↓
Lambda (via Execution Role)
   ↓ allows Lambda to call
DynamoDB / CloudWatch Logs
   ↓
ECS Task (via Task Role)
   ↓ allows containers to call
RDS / SQS / SNS
```

**Why each connection exists:** No AWS service can call another AWS service without an IAM identity (user, role, or resource policy) explicitly permitting it. EC2 doesn't get to read S3 "because it's in the same account" — it needs an attached **IAM Role** (called an Instance Profile when attached to EC2). Same logic applies to Lambda's Execution Role, ECS Task Role, etc. IAM is the permission layer that every other service checks before honoring a request.

### 13.7 Terminal Workflow

A DevOps engineer's typical IAM setup from a fresh Ubuntu terminal:

```bash
# 1. Confirm CLI installed and configured
aws --version
aws configure

# 2. Confirm current identity (should be root or bootstrap admin)
aws sts get-caller-identity

# 3. Create a dedicated admin IAM user (stop using root)
aws iam create-user --user-name admin-user
aws iam attach-user-policy --user-name admin-user \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess

# 4. Create access keys for that user
aws iam create-access-key --user-name admin-user
# → copy AccessKeyId + SecretAccessKey somewhere safe

# 5. Reconfigure CLI to use the new user instead of root
aws configure
# paste the new access key/secret

# 6. Verify the switch worked
aws sts get-caller-identity
# Arn should now show admin-user, not root

# 7. Create a service role (for EC2 to access S3 later)
aws iam create-role --role-name EC2-S3-Role \
  --assume-role-policy-document file://trust-policy.json
aws iam attach-role-policy --role-name EC2-S3-Role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# 8. Create an Instance Profile and add the role to it (needed before attaching to EC2)
aws iam create-instance-profile --instance-profile-name EC2-S3-Profile
aws iam add-role-to-instance-profile \
  --instance-profile-name EC2-S3-Profile \
  --role-name EC2-S3-Role
```

### 13.8 Verification

```bash
aws iam list-users
```
**Reading the output:** look for a JSON array under `Users`. Each entry has `UserName`, `UserId`, `Arn`, `CreateDate`. If your new user appears, creation succeeded.

```bash
aws iam list-attached-user-policies --user-name admin-user
```
Confirms which managed policies are attached — should list `AdministratorAccess` (or whatever you attached).

```bash
aws iam get-role --role-name EC2-S3-Role
```
Confirms the role exists and shows its trust policy (`AssumeRolePolicyDocument`) — should show `ec2.amazonaws.com` as the trusted principal.

```bash
aws sts get-caller-identity
```
Confirms which identity your CLI is currently acting as — critical sanity check before running any other command.

### 13.9 Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| `An error occurred (AccessDenied)` | Current identity lacks the IAM action permission | Switch to an admin identity, or attach the missing permission |
| `InvalidClientTokenId` | Access key is wrong/deleted/rotated | Re-run `aws configure` with a valid key pair |
| `SignatureDoesNotMatch` | Secret key was copied incorrectly (extra space, wrong char) | Recreate the access key and re-paste carefully |
| CLI hangs or times out | No internet / wrong region set | Check `aws configure get region`, verify network |
| Role won't attach to EC2 | Used Role name instead of Instance Profile name | EC2 needs an **Instance Profile**, not a bare Role — create one and add the role to it |
| "User is not authorized to perform sts:AssumeRole" | Trust policy doesn't include the correct principal | Edit trust policy to include the correct service/account ARN |

**Debugging commands:**
```bash
aws configure list          # shows which credentials/region are active
aws sts get-caller-identity # confirms identity
aws iam get-user            # confirms your own user details
```
There are no "log files" for IAM itself — but **CloudTrail** records every IAM API call made in your account (`CloudTrail → Event history`), the go-to place to debug "who did what."

### 13.10 Real-World Workflow

```
Developer joins team
   ↓
Admin creates IAM User (or adds to SSO/Identity Center)
   ↓
User assigned to an IAM Group (e.g. "Developers")
   ↓
Group has a Policy limiting access (e.g. only dev environment, no billing access)
   ↓
CI/CD pipeline (GitHub Actions) uses a dedicated IAM Role via OIDC — NOT long-lived keys
   ↓
That Role has permissions scoped to deploy only to specific services (ECS, S3, CloudFormation)
   ↓
EC2 / ECS / Lambda use their own service Roles to access RDS, S3, CloudWatch
   ↓
CloudTrail logs every action for audit/compliance
```

In production, companies almost never issue long-lived IAM access keys to humans or CI pipelines anymore — they use **IAM Identity Center (SSO)** for humans and **OIDC-based role assumption** for CI/CD, minimizing leaked-credential risk.

### 13.11 Mini Lab

Complete this using **only the terminal**:

1. Create a new IAM user named `lab-user`.
2. Attach the `AmazonS3ReadOnlyAccess` policy to `lab-user` (not full admin this time).
3. Generate an access key for `lab-user`.
4. Configure a new AWS CLI profile called `lab` using those credentials:
   ```bash
   aws configure --profile lab
   ```
5. Using `--profile lab`, run `aws s3 ls` and confirm it works.
6. Using the same profile, try `aws ec2 describe-instances --profile lab` — it should **fail** with `AccessDenied` (proving the permission scoping worked).
7. Clean up:
   ```bash
   aws iam delete-access-key --user-name lab-user --access-key-id <KEY_ID>
   aws iam detach-user-policy --user-name lab-user --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
   aws iam delete-user --user-name lab-user
   ```

> ✅ Once this lab is done and understood, update the Progress Tracker and move to **Service 02 — EC2**, which will reuse the Role/Instance Profile pattern learned here.