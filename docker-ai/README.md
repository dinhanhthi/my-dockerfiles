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

## Requirement

You have successfully installed GPU driver on your (linux) machine.


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
docker build -t img_docker_ai . -f Dockerfile
# AFTER BUILD: ~13GB image!!!!

# create a container
docker-compose -p "container_ai" up -d
```

``` bash
# check gpu availability
nvidia-smi

# check cuda version
nvcc --version | grep "release"
```

``` bash
# check tensorflow version
pip show tensorflow-gpu

# check torch version
pip show torch
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

## Upgrade to a newer version of tensorflow?

1. Check if there are this version [on dockerhub](https://hub.docker.com/r/tensorflow/tensorflow/tags/?page=1&ordering=last_updated).
2. Check the version of `CUDA` in this docker image version. Check if there is a corresponding version [on Torch](https://pytorch.org/)? If **not**, don't upgrade!
3. Modify file **Dockerfile**:
   1. Replace all current version with the newer version (using _Find and replace_ of the IDE)
   2. Relace the line under `# TORCH` with the one on [Torch website](https://pytorch.org/).
4. Build "another" image (with different name, just in case we fail, we still have the old one).
5. Modify **docker-compose.yml** with the "newer" name of image.
6. Create "another" container following section [Build and Run](#build-and-run) (replace `"container_ai"` with "another").

## References

1. Github: [tensorflow dockerfiles](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles/dockerfiles)
