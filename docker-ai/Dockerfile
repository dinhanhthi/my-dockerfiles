FROM tensorflow/tensorflow:2.4.3-gpu
# CHECK VERSION ON 14/04/22
# Because torch doesn't have any image for 11.2 where all newer version of tensorflow (upto 2.8.*) is using cuda 11.2,
#   we keep using 2.4.3 and wait!
# https://hub.docker.com/layers/tensorflow/tensorflow/tensorflow/2.4.3-gpu/images/sha256-416e7c76297cfaf90f656d189684163095ce266e0f61c550f934daada8f03126?context=explore
# CUDA=11.0 CUDNN=8.0.4.30-1 CUDNN_MAJOR_VERSION=8
# LIBNVINFER=7.1.3-1

# Already installed python packages:
#   tensorflow-gpu==2.4.3 (NOT tensorflow==2.4.3)
# RUN python3 -m pip install tensorflow==2.4.3

# fix (tzdata)
ARG DEBIAN_FRONTEND=noninteractive

# USEFUL APPS
RUN apt-get -y update
RUN apt-get install -y locales git r-base nano vim

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
RUN python3 -m pip install jupyterlab==3.2.9
# RUN jupyter labextension install @jupyterlab/toc

# TORCH
RUN pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

# OPENSSH
# ------ Uncomment below -----
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:qwerty' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
# need?
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
# Export port ssh
EXPOSE 22
ENTRYPOINT $(which sshd) -Ddp 22
# ---------------------------------


# Only display 3 last folder in the path
RUN echo 'PROMPT_DIRTRIM=3' >> ~/.bashrc

# Run jupyter notebook
CMD /bin/bash -c 'jupyter lab --no-browser --allow-root --ip=0.0.0.0 --NotebookApp.token="" --NotebookApp.password=""'
