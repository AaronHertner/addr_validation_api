# Use the official Python 3.9 image as the base image
FROM us-docker.pkg.dev/google-containers/python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8080

# Command to run the FastAPI app using Uvicorn
CMD ["python", "main.py"]