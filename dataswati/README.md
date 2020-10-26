## Dockerfile with Dataswati

An example of dockerfile which was used when I worked at Dataswati. This is a copy to see the work, there are some secret files which are not presented here. For more, check [this repo](https://github.com/dinhanhthi/git_dataswati).

Using with GPUs + Data Controller (working with pytorch, not tensorflow!),

``` bash
# create an image
docker build -t img_datas_dc . -f Dockerfile.nvidia_dc

# create a container
docker run --name docker_thi_dc --gpus all \
    -v /home/thi/git/dataswati/git/DataDisk/:/srv/DataDisk/ \
    -v /home/thi/git/dataswati/git/:/srv/ \
    -v /home/thi/git/dataswati/python-dataswati/popai/:/usr/lib/python3/dist-packages/popai \
    -v /home/thi/git/dataswati/git/data_controller/:/data_controller/ \
    -v /home/thi/git/dataswati/git/grpc_proto/:/data_controller/src/protos/ \
    --env-file /home/thi/git/git_dataswati/docker-thi/.env \
    -dp 8888:8888 \
    -w="/srv" -it img_datas_dc
```