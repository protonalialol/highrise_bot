# Use an official Python runtime as a parent image
FROM arm64v8/python:3.11.2-alpine3.16

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy rest of the stuff
COPY . /app

# Set BOT_VERSION environment variable
ARG BOT_VERSION
ENV BOT_VERSION $BOT_VERSION

# Set BOT_ADMINISTRATOR environment variable
ARG BOT_ADMINISTRATOR
ENV BOT_ADMINISTRATOR $BOT_ADMINISTRATOR

# Set BOT_ADMINISTRATOR_ID environment variable
ARG BOT_ADMINISTRATOR_ID
ENV BOT_ADMINISTRATOR_ID $BOT_ADMINISTRATOR_ID

# Set the environment variable PYTHONUNBUFFERED to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set the entry point to run the Python application
#ENTRYPOINT ["python", "main.py"]
ENTRYPOINT "highrise" "bots:$BOT_TYPE" $ROOM_ID $API_KEY
