FROM python:3.9

# set Working Directory
WORKDIR /app

# COPY requirements.txt .
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose Port
EXPOSE 5001

# Copy all files to target machine 
COPY . .

# Run this add.py as startup
CMD ["python", "add.py"]
