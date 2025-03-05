"""
This module contains the tasks that can be executed using the invoke command.
"""

from invoke import task


@task(name="install", aliases=["i"])
def install_dependencies(c):
    """
    Install the project dependencies listed in requirements.txt.
    """
    c.run("pip install --upgrade pip")
    c.run("pip install -r requirements-dev.txt")


@task(name="format", aliases=["f"])
def format_code(c):
    """
    Format the source code using black.
    """
    print("Formatting code ...")
    c.run("black .")


@task(name="lint", aliases=["l"], pre=[format_code])
def lint_code(c):
    """
    Lint the source code using pylint.
    """
    print("Genreating docker compose file ...")
    c.run("python generate_docker_compose.py")

    print("Checking code style ...")
    c.run("pylint --rcfile=.pylintrc .")

    print("Checking types ...")
    c.run("mypy .")


@task(name="run", aliases=["r"])
def run_app(c):
    """
    Run the application.
    """
    c.run("docker-compose up")


@task(name="build", aliases=["b"])
def build_images(c):
    """
    Build the Docker images.
    """
    print("Building Docker images ...")
    c.run("docker-compose build")
