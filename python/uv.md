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

Note: uv only works with versions of python beyond 3.7

List available versions fo python

```shell
uv python list
```

Installing Python 3.8

```shell
uv python install 3.8
```

Uninstalling Python 3.8

```shell
uv python uninstall 3.8
```

Updating to the latest version 

```Shell
uv self update
```

Running a pythgon script

```shell
uv run main.py
```

Specify a python version

```shell
uv run --python 3.9.21 main.py
```

Using dependencies with uv

```shell
uv run --with rich --requests --python 3.9 main.py
```

```shell
uvinit --script main.py --python 3.9.21
uv run
```

```shell
# Add comment metatdata to the script so that uv knows about the dependencies
uv add --script main.py "rich"
uv add --script main.py "requests"
```

## Working with Python projects

```shell
# Initialize a new project in the current directory.
uv init
```

```shell
# Initialize a new project in the my-dir directory.
uv init my-dir
```

This will create a few different files

- .gitignore
- .python-version
- main.py
- pyproject.toml
- README.md

It will also initialize the git repository.

uv also automatically creates a virtual environment for you.

### Installing a dependency

Given that we have initialized a project using `uv init`,
we can now add a dependency using `uv add`

```shell
# Use uv to add requests as a dependency to the current project
uv add requests
```

```shell
# Use uv to add a pinned version of the requests module to the current project
uv add requests==2.32.1
```

Notice that uv is creating a uv.lock file that includes version information.
You want to include this in git.


it should resolve the package and install the dependencies in 
the pyproject.toml file

### Removing a dependency

```shell
uv remove requests
```

This will update the pyproject.toml file removing requests as a dependency
and uninstalling it from the managed .venv virtual environment, and updating
the uv.lock file as well.

Also note that when running main.py with uv it automatically utilizes
the managed virtual environment `.venv`

```shell
uv run main.py
```

If you try to run this without the uv prefix you will likely run into
issues unless you've sourced the virtual environment. Using uv
makes this simpler because you no longer have to constantly do that,
just use uv to manage it implicitly.


If you add dependencies to pyproject.toml directly you will notice
that `uv run main.py` will automatically detect that the new dependency
is not present in the virtual environment and will install it.

This is because uv implicitly runs the `uv sync` command which 
automatically syncs the virtual environment from the project.toml.

### Regenerating the `uv.lock` file

```shell
# Regenerate the uv.lock file based on your current project settings.
uv lock
```



## Usage

### Installing 

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

### Installing the latest Python version

```shell
uv python install
```

This will install a uv-managed Python version even if there is already a 
Python installation on your system. If you've previously installed Python
with uv, a new version will not be installed.

Once Python is installed, it will be used by uv commands automatically.

### Viewing Python installations

```Shell
uv python list
```

### Installing multiple versions of python

```shell
uv python install 3.10 3.11 3.12
```

### Creating a virtual environment

```Shell
uv venv
```

This will create a new virtual environment and download a managed
Python version if Python is not found.

```shell
uv venv --python 3.12.0
```

### Running a script

```shell
uv run hello.py
```


## References

- [Documentation](https://docs.astral.sh/uv/)
- [GitHub](https://github.com/astral-sh/uv)
