import marimo

__generated_with = "0.11.14"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        """
        # Docker

        ## List Docker Images

        ```shell
        docker images
        ```

        ## List Docker Containers

        ```shell
        docker ps
        ```

        This command will show all running containers. If you want to see all containers, including stopped ones, use:

        ```shell
        docker ps -a
        ```

        ## Remove All Dangling Images (images that are not tagged and are not referenced by any container)

        ```shell
        docker image prune
        ```

        If you want to remove all unused images (not just dangling ones), you can use the `-a` flag:

        ```shell
        docker image prune -a
        ```

        You can also add the `-f` flag to force the prune operation without confirmation:

        ```shell
        docker image prune -a -f
        ```

        ## Removing Stopped Containers

        You can delete a stopped Docker container using the following command:

        ``` shell
        docker rm <container_id_or_name>
        ```

        Note: The `container_id_or_name` does not need to be complete.  You can use a unique prefix of the container ID or the full container name. For example, if the container ID is `1234567890ab` you can use just the first few characters as long as they uniquely identify the container:

        ### Example of using a prefix to delete a stopped Docker container

        ```shell
        docker rm 123
        ```

        where 

        To remove all stopped containers in Docker, you can use the `docker container prune` command. This command will remove all stopped containers.

        ```shell
        docker container prune
        ```

        If you want to force the prune operation without confirmation, you can add the `-f` flag:

        ```shell
        docker container prune -f
        ```

        ## Running a Docker image

        To run a Docker image, you can use the `docker run` command followed by the image name.

        ```shell
        docker run <image_name>
        ```

        For example, to run the `marimo-postgres-notebook` image, you would use:

        ```shell
        docker run marimo-postgress-notebook
        ```

        If you need to map pports, set environmetn variables, or specify a container name, you can add additional options.

        ```shell
        docker run -d -p 9090:8080 -name postres_notebook_container --env-file .env marimo-postgres-notebook
        ```

        - `docker run`: The base command to create and start a new container
        - `-d`: Runs the container in detached mode, meaning it runs in the background
        - `-p 9090:8080`: Maps port 9090 on the host to port 8080 in the container. This allows you to access the application running inside the container via port 9090 on your host machine.
        - `--name postgres_notebook_container`: Assigns a name to the container, making it easier to reference.
        - `--env-file .env`: Specifies an environment file to set environmetn varialbes inside the container.
        - `marimo-postgres-notebook`: The name of the Docker image to use for creating the container.

        ## Running a Docker image interactively

        You can start your Docker container interactively to debug it. You can do this by overring the entrypoint to start a shell instead of running the application.

        ```shell
        docker run -it --entrypoint /bin/sh <your_image_name>
        ```

        For example

        ```
        docker run -it --entrypoint /bin/sh marimo-docker-notebook
        ```
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
