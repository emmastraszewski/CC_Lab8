FROM python:3.8 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY .. .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD gunicorn -b 0.0.0.0:5000 app:app