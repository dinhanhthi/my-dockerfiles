FROM tensorflow/tensorflow:2.3.1-gpu
# https://hub.docker.com/layers/tensorflow/tensorflow/2.3.1-gpu/images/sha256-37c7db66cc96481ac1ec43af2856ef65d3e664fd7f5df6b5e54855149f7f8594?context=explore
# CUDA=10.1 CUDNN=7.6.4.38-1 CUDNN_MAJOR_VERSION=7
# LIBNVINFER=6.0.1-1

# Already installed python packages:
#   tensorflow-gpu==2.3.1 (NOT tensorflow==2.3.1)

# fix (tzdata)
ARG DEBIAN_FRONTEND=noninteractive

#
RUN apt-get install -y locales git r-base vim

# nodejs (enable extension for jupyter notebook)
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
# fix UnicodeDecodeError
RUN npm config set unicode false

# install python's requirements
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt
COPY . .

## Jupyter notebook's extensions
# RUN python3 -m jupyter labextension install @jupyterlab/toc

# TORCH
RUN pip3 install torch==1.7.0+cu101 torchvision==0.8.1+cu101 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

# Run jupyter notebook
CMD /bin/bash -c 'jupyter lab --no-browser --allow-root --ip=0.0.0.0 --NotebookApp.token="" --NotebookApp.password=""'