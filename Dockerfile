FROM python:3.8-slim

# Install ping
RUN apt-get update && apt-get install -y iputils-ping
RUN apt-get update && apt-get install -y \
    mpich \
    libmpich-dev
RUN pip install mpi4py

WORKDIR /app
COPY . /app

# Command
CMD ["tail", "-f", "/dev/null"]