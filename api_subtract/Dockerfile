FROM python:3.9

# Set Working Directory
WORKDIR /app

# COPY requirements.txt .
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port on which the Flask app will be running
EXPOSE 5002

# Copy application to target machine
COPY . .

# Run subtract.py as startup
CMD ["python", "subtract.py"]
