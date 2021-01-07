## Base Machine Learning & Data Science

This is the main docker setting up environement I've used so far for the purpose of learning and working by myself.

This dockerfile contains:

1. Python 3
2. Vim
3. Integrated NVIDIA GPU
4. Scikit-learn
5. Tensorflow (which supports GPU)
6. Pytorch (which supports GPU)
7. Jupyter notebook and some of its extensions.

And some python's libraries are given in [requirements.txt](./requirements.txt).

## Working dirs

``` bash
# Working folders & this repo should be
|-- git/
	|-- other working folders
	|-- my-dockerfiles/
		|-- docker-ai/
			|-- docker-compose.yml
			|-- Dockerfile
			|-- requirements.txt

# All dirs in /git/ should visible in the container "docker_ai"
# If there are any changes, changes the right dirs in docker-compose.yml
```

## Build and Run

``` bash
# build an image
docker build -t img_base_ml_data . -f Dockerfile

# create a container
docker-compose up -d
```

``` bash
# check gpu availability
nvidia-smi

# check cuda version
nvcc --version | grep "release"
```

``` python
# check: pytorch + gpu?
python3 # enter to python env

import torch
torch.cuda.is_available()
torch.cuda.get_device_name(torch.cuda.current_device())
```

``` python
# check: tensorflow + gpu?
python3 # enter to python env

import tensorflow as tf
tf.config.list_physical_devices('GPU')
```

## References

1. Github: [tensorflow dockerfiles](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles/dockerfiles)