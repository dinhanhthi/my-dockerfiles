## Base Machine Learning & Data Science

This is the main docker setting up environement I've used so far for the purpose of learning and working by myself.

__Note__: The `Dockerfile` is generated and modified using [deepo's generator](https://github.com/ufoym/deepo#Customization).

``` bash
# Generator the base Dockerfile from deepo
git clone https://github.com/ufoym/deepo.git
cd deepo/generator
python generate.py Dockerfile torch pytorch tensorflow opencv python==3.6 jupyter jupyterlab keras
```

This dockerfile contains:

1. Python 3
2. Vim
4. Integrated NVIDIA GPU
5. Scikit-learn
6. Tensorflow (which supports GPU)
7. Pytorch
8. Jupyter notebook and some of its extensions.

And some python's libraries are given in [requirements.txt](./requirements.txt).

## Build and Run

``` bash
# build an image

```

## References

1. Github: [tensorflow dockerfiles](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles/dockerfiles)