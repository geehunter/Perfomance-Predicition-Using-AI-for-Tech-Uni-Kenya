FROM python:3.8-slim-buster

MAINTAINER Austinstevesk

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install requirements.txt

COPY . .

CMD ["python", "app.py"]