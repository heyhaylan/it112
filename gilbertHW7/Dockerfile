# base image
FROM python:3.11-slim

# environment variable for project home
ENV DockerHOME=/app

# create directory
RUN mkdir -p $DockerHOME

# set working directory
WORKDIR $DockerHOME

# set python environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# upgrade pip
RUN pip install --upgrade pip

# copy files
COPY . $DockerHOME

# install requirements
RUN pip install -r requirements.txt

# expose Django's default port
EXPOSE 8000

# run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
