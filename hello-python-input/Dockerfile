# Use an official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local Python script into the container
COPY app.py .

# Use ENTRYPOINT to keep "python app.py" fixed
ENTRYPOINT ["python", "app.py"]
