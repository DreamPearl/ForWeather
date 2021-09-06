FROM python:latest

COPY . /app

RUN pip install Flask

WORKDIR /app

CMD [ "python3", "forweather.py" ]
