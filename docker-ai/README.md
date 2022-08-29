## Base Machine Learning & Data Science

This is the main docker setting up environement I've used so far for the purpose of learning and working by myself.

<details>
<summary>This dockerfile contains:</summary>

1. Python 3
2. Vim
3. Integrated NVIDIA GPU
4. Scikit-learn
5. Tensorflow (which supports GPU)
6. Pytorch (which supports GPU)
7. Jupyter notebook and some of its extensions.

And some python's libraries are given in [requirements.txt](./requirements.txt).
</details>

## Dockerfile

- `Dockerfile`: cuda 11.2 + tf 2.8.1 + torch 11.2+cu11.3 (!!)
- `Dockerfile.cu113`: no tf + cuda 11.3 (check [this base image](https://hub.docker.com/layers/cuda/nvidia/cuda/11.3.1-devel-ubuntu20.04/images/sha256-4c1ddee84918551d040c2d24581b4172fbd4734789908e9030f90d2bebf0afc9?context=explore)).
- `Dockerfile.cu113-cudnn8`: same as `.cu113` but with `cudnn 8.2.0.53` installed (check [this base image](https://hub.docker.com/layers/cuda/nvidia/cuda/11.3.1-cudnn8-devel-ubuntu20.04/images/sha256-459c130c94363099b02706b9b25d9fe5822ea233203ce9fbf8dfd276a55e7e95?context=explore))!

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
docker build -t img_ai . -f Dockerfile
# AFTER BUILD: ~13GB image!!!!

# create a container
docker-compose -p "container_ai" up -d

# Or using below
# (remove "bash" for images running the notebook <- check the Dockerfile)
docker run --name container_ai --gpus all \
  -v /home/thi/git/:/git/ \
  -dp 8888:8888 \
  -dp 6789:22 \
  -w="/git" -it img_ai bash
```

## Run from MacOS

***(Updated 20/04/22)***

<details>
<summary>For me only!</summary>

```bash
# Install and run NoMachine first!

# Take control Linux's terminal
ssh thi@pop-os.local

# Run the server
docker exec container_ai $(which sshd) -Ddp 22
# or
start_22

# Open notebook
ssh -N -L localhost:8888:127.0.0.1:8888 thi@pop-os.local

# Enter docker
# Make sure to run the server first (start_22)
ssh -p 6789 root@pop-os.local # qwerty
```
</details>

### Connect via ssh?

```bash
# Run ssh sever
docker exec container_ai $(which sshd) -Ddp 22

# ssh to container from current computer
ssh -p 6789 root@localhost
# enter "qwerty" as pwd
```

👉 Check more on [this note](https://dinhanhthi.com/local-connection-between-2-computers-ssh/).

### Checking GPU

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
2. Check the version of `CUDA` in this docker image version ([The list of corresponding versions between cuda and TF](https://www.tensorflow.org/install/source#gpu)). Check if there is a corresponding version [on Torch](https://pytorch.org/)? If **not**, don't upgrade!
3. Modify file **Dockerfile**:
   1. Replace all current version with the newer version (using _Find and replace_ of the IDE)
   2. Relace the line under `# TORCH` with the one on [Torch website](https://pytorch.org/).
4. Build "another" image (with different name, just in case we fail, we still have the old one).
5. Modify **docker-compose.yml** with the "newer" name of image.
6. Create "another" container following section [Build and Run](#build-and-run) (replace `"container_ai"` with "another").

## References

1. Github: [tensorflow dockerfiles](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles/dockerfiles)
