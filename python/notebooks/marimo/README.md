# Using Marimo Notebooks

This document contains my personal notes on Marimo Notebooks.

## Docker

Since I've added a new Dockerfile and a docker-compose.yaml file, I can now run the Marimo Notebooks in separate Docker containers.

Each time you create a new notebook, it will be saved in the `notebooks` directory.

In order to make it available via `docker-compose up`, you need to add the following line to the `docker-compose.yaml` file:

```yaml
  docker_app:
    image: marimo-notebook-<notebook-name>
    build:
      context: .
      dockerfile: Dockerfile
      args:
        NOTEBOOK_NAME: <notebook-name>
    container_name: marimo-container-<notebook-name>
    ports:
      - "<notebook_port>:8080"
```

Where the notebook_ports must be unique for each notebook, and the `notebook-name` must be the name of the notebook file without the `.md` extension.

If the code in your notebook requires a custom environment you will need to specify an environment file for your service

```yaml
  docker_app:
    image: marimo-notebook-<notebook-name>
    build:
      context: .
      dockerfile: Dockerfile
      args:
        NOTEBOOK_NAME: <notebook-name>
    container_name: marimo-container-<notebook-name>
    ports:
      - "<notebook_port>:8080"
    env_file:
      - <env-file>
```

There could be a single `.env` file for all the notebooks, or a separate `.env` file for each notebook.
It merely needs to be specified in the `docker-compose.yaml` file, and depends on the requirements of the notebook in question.

## Setup

### Install

Setup Marimo in a new Virtual environment
```shell
mkdir example
cd example
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install marimo

# Install a few commonly utilized dependencies
pip install -r requirements.txt
```

View the Help menu

```shell
marimo --help
```

View the tutorial list

```shell
marimo tutorial --help
```

## Recommended Tutorial Sequence

Marimo recommends the following tutorial sequence
for people new to the platform:

1. intro
2. dataflow
3. ui
4. markdown
5. sql
6. layout
7. fileformat
8. markdown-format
9. for-jupyter-users

To view the tutorial list

```shell
marimo tutorial --list
```

To get started with the intro tutorial:

```shell
marimo tutorial intro
```

This will start the intro tutorial in the default browser.

### Usage

Running the tutorial

```shell
marimo tutorial intro
```

### Creating a new notebook

```shell
marimo new python/notebooks/marimo.md
```

### Viewing the notebook

```shell
marimo view python/notebooks/marimo.md
```



## References

- [GitHub](https://github.com/marimo-team/marimo)
- [Documentation](https://docs.marimo.io/)
- [GitHub Notebooks On-The-Fly](https://marimo.io/blog/github-notebooks-on-the-fly)