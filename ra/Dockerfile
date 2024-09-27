# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL client for connecting to the database
RUN apt-get update && apt-get install -y postgresql-client

# Copy the rest of the application code
COPY ra.py ./

# Expose the HTTPS port
EXPOSE 443

# Run the application
CMD ["python", "ra.py"]
