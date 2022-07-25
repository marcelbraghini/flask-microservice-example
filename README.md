# flask-microservice-example

### For run microservice

Install dependencies
```bash
pip3 install -r requirements.txt
```

Up server
```bash
$ bin/server
```

```bash
$ FLASK_CONFIG="development" flask run -h localhost -p 5000

$ FLASK_CONFIG="development" gunicorn --bind 0.0.0.0:5000 wsgi:app
```

### Docker image

For build image
```bash
docker image build -t flask_microservice_example .
```

For run container
```bash
docker run -p 5000:5000 -d flask_microservice_example
```

CURLs: 
```
curl --location --request POST 'localhost:5000/history-action' \
--header 'Content-Type: application/json' \
--data-raw '{ 
    "actionName": "WEGE3F.SA",
    "startDate": "2022-01-01",
    "endDate": "2022-07-30"
}'

curl --location --request POST 'localhost:5000/current-action' \
--header 'Content-Type: application/json' \
--data-raw '["TAEE4F.SA"]'

curl --location --request POST 'localhost:5000/current-action' \
--header 'Content-Type: application/json' \
--data-raw '["TAEE4F.SA", "WEGE3F.SA"]'
```
