##  🐳 My Dockerfile

👉 **My note**: [Docker](https://dinhanhthi.com/docker/).



### Quick docker commands

```bash
# Build an image
docker build -t <image_name> . -f Dockerfile

# Create a container
docker run --name container_ai --gpus all -v /home/thi/git/:/git/ -dp 8888:8888 -dp 6789:22 -w="/git" -it img_ai bash

# List all containers
docker ps -a

# List all images
docker images

# Delete
docker rm <container_name/id>
docker iamge rm <image_name/id>

# List all dangling images
docker images -f dangling=true
```



### Quick test & check info

```bash
# Check os info
cat /etc/os-release

# check gpu availability
nvidia-smi

# check cuda version
nvcc --version | grep "release"
```

```bash
# Check version
pip show tensorflow
pip show tensorflow-gpu
pip show torch
```

```bash
# check: pytorch + gpu?
python3 # enter to python env

import torch
torch.cuda.is_available()
torch.cuda.get_device_name(torch.cuda.current_device())
# check: tensorflow + gpu?
python3 # enter to python env

import tensorflow as tf
tf.config.list_physical_devices('GPU')
```



