# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Copy the project files into the container
COPY . /app

# Expose port 8000 for Django
EXPOSE 8000

# Default command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "librarysystem.wsgi:application"]