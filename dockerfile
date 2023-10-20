#Esta línea establece la imagen base que utilizarás para tu contenedor, en este caso, Python 3.9 en una versión liviana (slim)

FROM python:3.9-slim

#Esta línea establece el directorio de trabajo dentro del contenedor en "/app"
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt /tmp/requirements.txt

# Install any needed packages specified in requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

#Esta línea expone el puerto 8080 del contenedor al mundo exterior, 
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
