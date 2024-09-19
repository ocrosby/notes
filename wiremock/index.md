# Wiremock

Wiremock is a tool for mocking HTTP services. It can be used to simulate the behavior of a real service, and can be used to test the behavior of a service that is not yet implemented.


## Quick Start

Pull the Docker image

```shell
docker pull wiremock/wiremock:latest
```

Checkout the demo repository

```shell
git clone https://github.com/wiremock/wiremock-docker.git
```

Start the WireMock instance

```shell
docker run -it --rm \
  -p 8080:8080 \
  -v $PWD/wiremock-docker/samples/hello/stubs:/home/wiremock \
  wiremock/wiremock:latest
```

- docker run: Runs a command in a new container
- -it: Interactive mode
- --rm: Automatically remove the container when it exits
- -p 8080:8080: Maps port 8080 on the host to port 8080 on the container
- -v $PWD/wiremock-docker/samples/hello/stubs:/home/wiremock: Mounts the stubs directory from the host to the /home/wiremock directory in the container
- wiremock/wiremock:latest: The name of the image to run

## Configuration

You can configure WireMock as follows:

- Passing the CLI arguments
- Passing Environment variables
- Passing configuration files via volumes
- Building a custom image using wiremock/wiremock as a base image

### Passing the CLI arguments

```shell
docker run -it --rm -p 8443.9443 wiremock/wiremock --https-port 8443 --verbose
```

This command starts a WireMock instance with the HTTPS port set to 8443 and verbose logging enabled.

### Using environment variables

The following environment variables are supported by the image

* uid: the container executor uid, useful to avoid file creation owned by root
* JAVA_OPTS: for passing any custom options to Java e.g. -Xmx128m
* WIREMOCK_OPTS: for passing any custom options to WireMock e.g. --https-port 8443

```shell
docker run -it --rm \
  -e WIREMOCK_OPTIONS='--https-port 8443 --verbose' \
  -p 8443.9443 \
  --name wiremock \
  wiremock/wiremock:latest
```

### Passing configuration files as volumes

Inside the container, the WireMock uses `/home/wiremock` as the default directory for storing the stubs and mappings. You can mount the host directory to this location to persist the data.

```shell
docker run -it --rm \
  -p 8080:8080 \
  -v $PWD/wiremock-docker/samples/hello/stubs:/home/wiremock \
  wiremock/wiremock:latest
```

### Building a custom image

You can build a custom image using the wiremock/wiremock image as the base image. You can add your custom configuration files and scripts to the image.

```dockerfile
# Sample Dockerfile
FROM wiremock/wiremock:latest
COPY wiremock /home/wiremock
ENTRYPOINT ["/docker-entrypoint.sh", "--global-response-templating", "--disable-gzip", "--verbose"]
```
