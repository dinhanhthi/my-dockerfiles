## Quick Jekyll setting up

We don't need to install ruby, bundler,... to the host system.

``` bash
# clone a jekyll theme, e.g. dinhanhthi.com
mkdir ~/Downloads/test
cd ~/Downloads/test
git clone git@github.com:dinhanhthi/dinhanhthi.com.git
cd dinhanhthi.com

# copy folder "docker" to the root of the jekyll site, e.g. "dinhanhthi.com/docker"
cd docker
docker-compose -p "project_name" up -d
# You should use differnet project_name for different jekyll sites 
# if you run simultaneously multiple jekyll sites

# whenever working
docker start dat_local
```

An example of using an additional script is given in repo [dinhanhthi.com](https://github.com/dinhanhthi/dinhanhthi.com).