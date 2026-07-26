# Install the virtual environment package (if not already installed)

sudo apt update
sudo apt install python3-venv

# Create a virtual environment

python3 -m venv .venv

# Activate it

source .venv/bin/activate

# Upgrade pip

python -m pip install --upgrade pip

# Install boto3

python -m pip install boto3

# Verify

python -c "import boto3; print(boto3.**version**)"
