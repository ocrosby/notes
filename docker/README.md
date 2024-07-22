# Docker

## Managing Containiner Images

Container images use layered filesystems via UnionFS.  Modifications are stored in a new layer.

```bash
> git clone https://github.com/sandervanvugt/containers
> cd containers
> ls
> cd sandertest/
```

View the help menu for the docker command

```Shell
docker --help
```


View all containers running on the local machine

```Shell
docker ps
```

Show all containers on the local machine (even the ones that aren't running)

```Shell
docker ps -a
```

Note: docker start can only start stopped containers

This command to run ubuntu latest exits immediately
docker run ubuntu:latest


Starting an interactive terminal in an ubuntu container

```Shell
docker run -it ubuntu /bin/bash
```

Prune dangling Docker images

```sh
docker image prune -a -f
```
