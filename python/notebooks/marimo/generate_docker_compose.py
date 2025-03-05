"""
Generate a docker-compose.yaml file by reading the file names from the notebooks directory
"""

import os
import yaml


class CustomDumper(yaml.Dumper):
    """
    Custom YAML Dumper to add an extra line break between services.
    """

    def write_line_break(self, data=None):
        """
        Write a line break in the YAML output.

        :param data: Data to write (default is None)
        """
        super().write_line_break(data)
        if len(self.indents) == 1:
            super().write_line_break()


def generate_docker_compose(notebooks_dir: str, output_file: str) -> None:
    """
    Generate a docker-compose.yaml file by reading the file names from the notebooks directory
    and assigning a new port starting from 8080, incrementing by one for each notebook found.

    :param notebooks_dir: Directory containing the notebook files
    :param output_file: Output file path for the generated docker-compose.yaml
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
        yaml.dump(docker_compose, file, Dumper=CustomDumper, default_flow_style=False)


if __name__ == "__main__":
    generate_docker_compose("notebooks", "docker-compose.yaml")
