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

export JEKYLL_VERSION=4.1.0
# Check more versions here: https://hub.docker.com/r/jekyll/jekyll/tags

# build + serve (1st time)
docker run --name dat.com --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:$JEKYLL_VERSION jekyll serve -I
# goto http://localhost:4000

# later uses
# it runs with "bundle exec jekyll serve -I"
docker start dat.com

# build all site in container dat.com
docker exec -it dat.com jekyll build
```

An example of using an additional script is given in repo [dinhanhthi.com](https://github.com/dinhanhthi/dinhanhthi.com).