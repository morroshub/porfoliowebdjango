# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /requirements.txt /tmp/requirements.txt

# # Install any needed packages specified in requirements.txt
# RUN set -ex && \
#     pip Install --upgrade pip && \
#     pip install -r /tmp/requirements.txt && \
#     rm -rf /root/.cache/ 

# # Make port 8080 available to the world outside this container
# EXPOSE 8080

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# CMD ["python", "app.py"]
