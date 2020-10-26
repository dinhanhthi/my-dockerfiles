## Quick checking docker + GPUs

My [notes](https://dinhanhthi.com/docker-gpu) about Docker + GPUs.

``` bash
# create an image
docker build -t img_quick_test_gpu .

# create a container
docker-compose up -d

# enter to test
docker exec -it docker_thi_test_gpu bash

# gpu available?
nvidia-smi
```