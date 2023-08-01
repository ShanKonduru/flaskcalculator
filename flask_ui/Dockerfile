# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask UI application to the container's working directory
COPY . .

# Expose the port on which the Flask app will be running
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
