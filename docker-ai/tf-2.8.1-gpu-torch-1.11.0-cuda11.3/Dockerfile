FROM tensorflow/tensorflow:2.8.1-gpu-jupyter
# https://hub.docker.com/layers/tensorflow/tensorflow/tensorflow/2.8.1-gpu-jupyter/images/sha256-844c2c9aa67313706158621170d99d0a04ed8617637422230281c769883773dc?context=explore

# fix (tzdata)
ARG DEBIAN_FRONTEND=noninteractive

# USEFUL APPS
RUN apt-get -y update
RUN apt-get install -y locales git r-base vim

# install python's requirements
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt
COPY . .

# TORCH
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

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
