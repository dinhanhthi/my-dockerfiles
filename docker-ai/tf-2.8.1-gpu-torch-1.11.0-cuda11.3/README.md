## tf2.8.1 + torch 1.11.0 + cuda 11.3 + gpu + jupyter

- First test on Google's Vertex Workbench (use the machine of Compute Engine).
- This folder contains only `Dockerfile`, it's not enough, checkout other folders too.

```bash
# Quick
docker build -t image_name . -f Dockerfile
docker create --gpus all --name container_ai -t -i image_name bash
docker start container_ai
docker exec -it container_ai bash
```

```bash
pip show tensorflow
pip show torch
python3
```

```python
import torch
torch.cuda.get_device_name(torch.cuda.current_device())

import tensorflow as tf
tf.config.list_physical_devices('GPU')
```