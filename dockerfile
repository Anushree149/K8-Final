# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN gunicorn --version
# Copy the entire Django project into the container
COPY . .

# Collect static files (optional, if you are serving static files)
RUN python manage.py collectstatic --noinput

# Run database migrations
# RUN python manage.py migrate
# Expose port 8000 for the application
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Command to run the application with gunicorn
CMD ["gunicorn", "My_To_do.wsgi:application" , "--bind", "0.0.0.0:8000"]
