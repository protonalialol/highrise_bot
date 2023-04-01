# Use an official Python runtime as a parent image
FROM arm64v8/python:3.11.2-alpine3.16

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
#RUN apt-get install vine -y

# Set the environment variable PYTHONUNBUFFERED to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set the entry point to run the Python application
#ENTRYPOINT ["python", "main.py"]
ENTRYPOINT "highrise" "demo:$BOT_TYPE" $ROOM_ID $API_KEY
