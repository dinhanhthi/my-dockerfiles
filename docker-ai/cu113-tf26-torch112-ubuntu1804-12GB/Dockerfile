FROM lablup/python-tensorflow:2.6-py38-cuda11.3
# Dockerhub: https://dockr.ly/3KqZyH1
# Github: https://bit.ly/3KtRPrt

# encoding
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf

# fix (tzdata)
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y python3-pip python3-dev

# alias
RUN echo 'alias python="python3"' >> ~/.bashrc
RUN echo 'alias pip="pip3"' >> ~/.bashrc
# only display 3 last folder in the path
RUN echo 'PROMPT_DIRTRIM=3' >> ~/.bashrc

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install jupyterlab==3.4.5
RUN pip3 install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113


# requirements
# COPY requirements.txt requirements.txt
# RUN python3 -m pip install --upgrade pip && \
#     python3 -m pip install -r requirements.txt
# COPY . .

# run
CMD /bin/bash -c 'jupyter lab --no-browser --allow-root --ip=0.0.0.0 --NotebookApp.token="" --NotebookApp.password=""'
