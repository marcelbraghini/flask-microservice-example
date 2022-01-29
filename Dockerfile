FROM python:3.9-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app/main

ENTRYPOINT ["python3"]

CMD ["init.py"]
