## Amazon Web Services (AWS) – Overview

AWS is a leading cloud computing platform by Amazon that provides on-demand access to IT resources such as servers, storage, databases, networking, security, and DevOps tools over the internet. Instead of buying and maintaining physical servers, users can rent computing power and services from AWS and pay only for what they use.

### Use Cases
AWS is widely used for:
- Hosting websites and applications
- Storing and processing large amounts of data
- Running DevOps pipelines and automation
- Building scalable microservices and APIs
- Machine learning, analytics, and IoT solutions

### Key Benefits
- **Scalability** – easily scale up or down
- **Reliability** – high availability across regions
- **Security** – built-in identity and access management (IAM)
- **Cost efficiency** – pay-as-you-go pricing

## AWS CLI Installation

### On Ubuntu / WSL
```bash
sudo apt update
sudo apt install awscli -y
```

### On Windows (PowerShell)
```powershell
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

## Configure AWS CLI

Run the configuration command:
```bash
aws configure
```

You will be asked for:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g. ap-south-1)
- Output format (json)

## Beginner AWS CLI Commands

### List S3 Buckets
```bash
aws s3 ls
```

### Create an S3 Bucket
```bash
aws s3 mb s3://my-first-bucket-ismail
```

### Upload a File to S3
```bash
aws s3 cp test.txt s3://my-first-bucket-ismail/
```

### Download a File from S3
```bash
aws s3 cp s3://my-first-bucket-ismail/test.txt .
```

### List EC2 Instances
```bash
aws ec2 describe-instances
```

### List IAM Users
```bash
aws iam list-users
```

## Common AWS Services

| Service | Description |
|---------|-------------|
| EC2     | Virtual servers |
| S3      | Object storage |
| IAM     | Users & permissions |
| RDS     | Managed databases |
| VPC     | Networking |
| Lambda  | Serverless functions |

## AWS EC2

### SSH Client Setup

#### Change File Permissions
```bash
chmod 400 "dev.pem"
```

#### Connect Using Public DNS
```bash
ssh -i ~/.ssh/dev.pem ubuntu@ec2-43-204-228-238.ap-south-1.compute.amazonaws.com
```

#### Connect Using Public IPv4 Address
```bash
ssh -i ~/.ssh/dev.pem ubuntu@43.204.228.238
```

### File Transfer

#### Upload Local File to EC2 (SCP - Secure Copy)
```bash
scp -i ~/.ssh/dev.pem -r /e/devops/Docker/project/backend ubuntu@43.204.228.238:~/backend
```

## Nginx Reverse Proxy Setup

### What is a Reverse Proxy?

A reverse proxy is a server that sits in front of backend servers and forwards client requests to them. It:
- Hides backend servers
- Improves security
- Enables load balancing
- Performs SSL termination
- Provides caching

**Flow:** Client → Nginx → Backend App

### Install Nginx (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

### Allow Firewall Access

```bash
sudo ufw allow 'Nginx Full'
sudo ufw reload
```

### Create Reverse Proxy Config

Edit the configuration file:
```bash
sudo nano /etc/nginx/sites-available/myapp
```

#### Example Configuration
```nginx
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Enable Configuration

```bash
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Nginx Management Commands

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
sudo nginx -t
```

### Network Connection Monitoring

```bash
# Show all network connections
sudo lsof -i -P -n

# Show only listening ports
sudo lsof -i -P -n | grep LISTEN
```

### Run Nginx in Background

```bash
sudo nohup nginx &
```
> Note: `nohup` allows nginx to continue running even if the terminal is closed

### Stop Nginx

```bash
sudo kill -9 $(sudo lsof -t -i:80)
```

### Log Files

- **Access Log:** `/var/log/nginx/access.log`
- **Error Log:** `/var/log/nginx/error.log`

## Summary

A reverse proxy with Nginx allows you to receive requests on port 80 and forward them to your application running on another port (e.g., 5000). This keeps your backend hidden and secure while providing a single entry point for clients.
