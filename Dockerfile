# base image
FROM python:3.10

#where your code lives
WORKDIR /app

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install dependencies
RUN pip install --upgrade pip


COPY requirements.txt .

#run this command to install all dependencies
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/merchex

#port where the django app runs
EXPOSE 8000

#start server
CMD python manage.py runserver 0.0.0.0:8000