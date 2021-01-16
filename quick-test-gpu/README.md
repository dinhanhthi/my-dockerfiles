## Quick checking docker + GPUs

My [notes](https://dinhanhthi.com/docker-gpu) about Docker + GPUs.

``` bash
# create an image
docker build -t img_quick_test_gpu .

# create a container
docker-compose run --rm jupyter

# enter to test
docker exec -it <name_of_container> bash

# gpu available?
nvidia-smi
```

``` bash
# Err: Unknown runtime specified nvidia
# Crreate the container by this
docker run --name docker_thi_test_gpu --gpus all -v /home/thi/git/:/srv/ -dp 8888:8888 -w="/srv" -it img_quick_test_gpu
```