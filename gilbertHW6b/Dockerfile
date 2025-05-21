# base image
FROM python:3.11-slim

# setup env variable
ENV DockerHOME=/Users/haylan/Desktop/it112/gilbertHW6b

# set work directory
RUN mkdir -p $DockerHOME

# where code lives
WORKDIR $DockerHOME

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip

# Copy project to docker home
COPY . $DockerHOME

# run this command to install all dependencies
RUN pip install -r requirements.txt

# port
EXPOSE 5000

# Run the Flask app using Python 3
CMD python gilbertHW6b.py runserver