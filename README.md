# flask-microservice-example

## Branch main  ----------

### For run microservice

Install dependencies
```bash
pip3 install -r requirements.txt
```

Up server
```bash
$ bin/server
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
