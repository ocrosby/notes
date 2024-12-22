# UV

UV is an extremely fast Python paackage manager and project manager, written in Rust.

## Features

- Fast installation times
- A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twwine, virtualenv, and more.
- 10-100x faster than pip
- Installs and manages Python versions
- Runs and installs Python applications
- Runs single-file scripts, with support for inline dependency metadata.
- Provides comprehensive project management, with a universal lockfile.
- Includes a pip-compatible interface for a performance boost with a familiar CLI.
- Supports Cargo-style workspaces for scalable projects
- Disk-space efficient, with a global cache for dependency deduplication.
- Installable without Rust or Python via curl or pip.
- Supports Windows, macOS, and Linux.

## Installation

```Shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```Shell
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```Shell
# With pip.
pip install uv
```

Updating to the latest version 

```Shell
uv self update
```

## Usage

### Initializing a new project

```shell
uv init example
```

This will create a new directory named example in the current directory.

You will need to change in that directory for remaining commands.

### Adding the requests package to the current workspace

```shell
uv add requests
```

### List the installed packages

```shell
uv pip list
```

## Install tools like ruff and invoke

```shell
uv tool install ruff
uv tool install invoke
```

To verify the installation of ruff

```shell
ruff --version
```

### Checking the project using ruff

```shell
uv run ruff check
```

### Installing multiple versions of python

```shell
uv python install 3.10 3.11 3.12
```

### Creating a virtual environment

```shell
uv venv --python 3.12.0
```

### Running a script

```shell
uv run hello.py
```


## References

- [GitHub](https://github.com/astral-sh/uv)