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

Initializing a new project

```Shell
uv init example

cd example

# Add packages
uv add requests

# List the installed packages
uv pip list

# Check the project
uv run ruff check

# Install a tool
uv tool install ruff
uv tool install invoke

ruff --version

uv python install 3.10 3.11 3.12

uv venv --python 3.12.0
```

Note: This will create a new project directory.

## References

- [GitHub](https://github.com/astral-sh/uv)