## Quick checking TF2 + GPUs

My [notes](https://dinhanhthi.com/tags#tensorflow) on Tensorflow.

``` bash
docker-compose run --rm jupyter

# in another terminal

# to check the name of the container
docker ps

# enter the container
docker exec -it <container_name> bash

# check if gpus are available?
nvidia-smi

# check if tf2 can use gpu?
python
import tensorflow as tf
tf.config.list_physical_devices('GPU')
```
