# flask-microservice-example

### For run microservice

Install dependencies
```bash
pip3 install -r requirements.txt
```

Up server
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

Links: 
```
https://www.thedigitalcatbooks.com/pycabook-chapter-04/
https://flask.palletsprojects.com/en/2.1.x/config/
https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/
https://flask.palletsprojects.com/en/2.1.x/blueprints/
```