FROM tensorflow/tensorflow:2.3.1-gpu

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install jupyterlab

CMD /bin/bash -c 'jupyter lab --no-browser --allow-root --ip=0.0.0.0 --NotebookApp.token="" --NotebookApp.password=""'
