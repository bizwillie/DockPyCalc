# Use an official Python runtime as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the calculator.py file into the container at /app
COPY calculator.py /app/calculator.py

# Specify the command to run the Python application within the container
CMD [ "python", "calculator.py" ]