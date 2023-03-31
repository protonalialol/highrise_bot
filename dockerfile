# Use a slim Ubuntu image as the base
FROM ubuntu:jammy

ENV PYTHONUNBUFFERED 1

# Install Python 3.11 and pip
RUN apt-get update 
RUN apt-get install -y python3.11
RUN apt-get install -y python3.11-distutils
RUN apt-get install -y python3-pip

# Set the working directory to /app
WORKDIR /app

# Copy the Python script into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python3.11 -m pip install --trusted-host pypi.python.org -r requirements.txt

# Set the environment variable PYTHONUNBUFFERED to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Run the Python script when the container starts
#ENTRYPOINT ["python3", "main.py"]
ENTRYPOINT ["highrise", "demo:Bot", "63c08fb2d0187c1745407652", "605989e0149119cb9095f303d86e43ea35eed73237fe52960c562800d8b277c5"]