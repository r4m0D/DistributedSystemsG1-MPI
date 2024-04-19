# Use a base image with Python pre-installed
FROM python:3.8-slim

# Install necessary system dependencies for mpi4py
RUN apt-get update && apt-get install -y \
    mpich \
    libmpich-dev

# Install mpi4py via pip
RUN pip install mpi4py

# Set the working directory in the container
WORKDIR /app

# Copy the MPI program files into the container
COPY . /app

# Default command to run when starting the container
CMD ["mpiexec", "-n", "4", "python", "trapezoidal_rule.py"]