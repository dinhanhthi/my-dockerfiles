# A simple python container

``` bash
# Build an image
docker build -t img_python . -f Dockerfile

# If using docker-compose
docker-compose -d up

# Without docker-compose (but have the same settings)
docker run --name python_container -t -dp 999:999 -w="/app" -v "$pwd:/app/" img_python

# Test
# http://0.0.0.0:9999
```