FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY  . .

# Set the entrypoint
ENTRYPOINT ["python" ]

# Run the app
CMD ["app.py"]
