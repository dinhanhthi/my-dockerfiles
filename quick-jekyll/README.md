## Quick Jekyll setting up

We don't need to install ruby, bundler,... to the host system.

``` bash
# pull jekyll image
docker pull jekyll/jekyll:4.1.0

# clone a jekyll theme, e.g. dinhanhthi.com
mkdir ~/Downloads/test
cd ~/Downloads/test
git clone git@github.com:dinhanhthi/dinhanhthi.com.git
cd dinhanhthi.com

# copy folder "docker" to the root of the jekyll site, e.g. "dinhanhthi.com/docker"

# build (once) the image
docker build -t jekyll_410 .

# build container
docker-compose up -d

# whenever working
docker start dat_local
```

An example of using an additional script is given in repo [dinhanhthi.com](https://github.com/dinhanhthi/dinhanhthi.com).