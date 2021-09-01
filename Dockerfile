FROM ubuntu:latest

COPY . /app

RUN apt-get update -y && apt-get install -y python3-pip python-dev

WORKDIR /

CMD [ "python3", "/app/forweather.py" ]
