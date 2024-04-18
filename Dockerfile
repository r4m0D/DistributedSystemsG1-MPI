# Use a base image with Python pre-installed
FROM python:3.8-slim

# Install necessary system dependencies for mpi4py
RUN apt-get update && apt-get install -y \
    mpich \
    libmpich-dev

# Set the working directory in the container
WORKDIR /app

# Set up a virtual environment in the directory /app/env
RUN python -m venv env

# Activate the virtual environment
ENV PATH="/app/env/bin:$PATH"

# Upgrade pip in the virtual environment
RUN pip install --upgrade pip

# Install mpi4py in the virtual environment
RUN pip install mpi4py

# Copy the MPI program files into the container
COPY . /app

# Default command to run when starting the container
CMD ["python3", "test.py"]
