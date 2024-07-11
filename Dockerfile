# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . /app

# Copy the database initialization script
COPY init_db.py /docker-entrypoint-initdb.d/init_db.py

# Wait for the database to be ready and run the initialization script
CMD ["sh", "-c", "while ! nc -z auth_db 5432; do echo 'Waiting for database...'; sleep 1; done; python /docker-entrypoint-initdb.d/init_db.py && python calculator.py"]
