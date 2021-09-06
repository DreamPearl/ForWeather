FROM python:latest

COPY . /app

RUN pip install Flask

WORKDIR /

CMD [ "python3", "/app/forweather.py" ]
