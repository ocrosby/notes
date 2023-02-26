# Docker

## Managing Containiner Images

Container images use layered filesystems via UnionFS.  Modifications are stored in a new layer.

```bash
> git clone https://github.com/sandervanvugt/containers
> cd containers
> ls
> cd sandertest/

```

docker --help

docker ps -a

Note: docker start can only start stopped containers

This command to run ubuntu latest exits immediately
docker run ubuntu:latest

whereas this one starts an interactive terminal
> docker run -it ubuntu /bin/bash

