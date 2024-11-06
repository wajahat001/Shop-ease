# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire User-Service folder to the container
COPY . /app/

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the environment variable for Flask to run on all IP addresses (0.0.0.0)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
