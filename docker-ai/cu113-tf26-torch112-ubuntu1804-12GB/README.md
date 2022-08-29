## README

❗ __BE CAREFUL__: This image takes **~37GB** after being extracted!!!

```bash
# Build image
docker build -t img_cu113_tf26_torch112 . -f Dockerfile
docker run --name container_cu113_tf26 --gpus all -v /home/thi/git/:/git/ -dp 8888:8888 -w="/git" -it img_cu113_tf26_torch112 bash
```

### Notes

- Installed successfully `detectron2`!