FROM tensorflow/tensorflow:2.4.0-gpu
# https://hub.docker.com/layers/tensorflow/tensorflow/2.4.0-gpu/images/sha256-67dbafa3e7918a3efc67db49063aebdb282a0ebb1c124b7ca0db18207e6d7a22?context=explore
# CUDA=11.0.3 CUDNN=8.0.4.30-1 CUDNN_MAJOR_VERSION=8
# LIBNVINFER=7.1.3-1

# Already installed python packages:
#   tensorflow-gpu==2.4.0 (NOT tensorflow==2.4.0)
# RUN python3 -m pip install tensorflow==2.4.0

# fix (tzdata)
ARG DEBIAN_FRONTEND=noninteractive

# USEFUL APPS
RUN apt-get -y update
RUN apt-get install -y locales git r-base vim

# NODEJS (enable extension for jupyter notebook)
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
# fix UnicodeDecodeError
RUN npm config set unicode false

# install python's requirements
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt
COPY . .

## Jupyter lab + its extensions
RUN python3 -m pip install jupyterlab==3.0.3
RUN jupyter labextension install @jupyterlab/toc

# TORCH
RUN pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

# OPENSSH
# RUN apt-get install -y openssh-server
# RUN mkdir /var/run/sshd
# RUN echo 'root:qwerty' | chpasswd
# RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# # SSH login fix. Otherwise user is kicked off after login
# RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
# # need?
# ENV NOTVISIBLE "in users profile"
# RUN echo "export VISIBLE=now" >> /etc/profile
# # Export port ssh
# EXPOSE 22
# CMD $(which sshd) -Ddp 22

# ALIAS


# Only display 3 last folder in the path
RUN echo 'PROMPT_DIRTRIM=3' >> ~/.bashrc

# Run jupyter notebook
CMD /bin/bash -c 'jupyter lab --no-browser --allow-root --ip=0.0.0.0 --NotebookApp.token="" --NotebookApp.password=""'
