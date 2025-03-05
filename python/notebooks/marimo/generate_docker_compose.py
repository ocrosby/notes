"""
Generate a docker-compose.yaml file for running multiple marimo notebooks in Docker containers.
"""

import os
import yaml


def generate_docker_compose(notebooks_dir: str, output_file: str) -> None:
    """
    Generate a docker-compose.yaml file for running multiple marimo notebooks in Docker containers.

    :param notebooks_dir:
    :param output_file:
    :return:
    """
    notebooks = [f for f in os.listdir(notebooks_dir) if f.endswith(".py")]
    services = {}
    port = 8080

    for notebook in notebooks:
        notebook_name = os.path.splitext(notebook)[0]
        service_name = f"marimo-notebook-{notebook_name}"
        container_name = f"marimo-container-{notebook_name}"

        services[service_name] = {
            "image": service_name,
            "build": {
                "context": ".",
                "dockerfile": "Dockerfile",
                "args": {"NOTEBOOK_NAME": notebook_name},
            },
            "container_name": container_name,
            "ports": [f"{port}:8080"],
        }
        port += 1

    docker_compose = {"services": services}

    with open(output_file, "w", encoding="utf-8") as file:
        yaml.dump(docker_compose, file, default_flow_style=False)


if __name__ == "__main__":
    generate_docker_compose("notebooks", "docker-compose.yaml")
