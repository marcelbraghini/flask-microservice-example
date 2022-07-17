FROM python:3.9-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "main.wsgi:app"]
