# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the Flask app runs on
EXPOSE 5000

# Define environment variable to prevent buffering
ENV PYTHONUNBUFFERED=1

# Run app.py when the container launches
CMD ["python", "app.py"]