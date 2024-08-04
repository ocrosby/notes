# SETUPTOOLS

Setuptools is a package that allows you to create Python packages that can be easily installed using the `pip` command.

## Features

- Create a `setup.py` file for your project
- Install your project using the `pip` command
- Include dependencies in your project
- Create a distributable package for your project
- Upload your package to the Python Package Index (PyPI)
- Install your package from PyPI
- Create a virtual environment for your project
- Create an editable installation for your project
- Create a standalone executable for your project
- Create a wheel package for your project
- Create a source distribution for your project
- Create a binary distribution for your project
- Create a universal distribution for your project
- Create a platform-specific distribution for your project
- Create a pure Python distribution for your project
- Create a C extension distribution for your project
- Create a FastAPI extension distribution for your project
- Create a Click extension distribution for your project
- Create a SQLAlchemy extension distribution for your project


## Installation

To create a `setup.py` file for your project, you need to create a Python file with the following content:

```Python
from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    py_modules=["myproject"],
    packages=find_packages(),
    install_requires=[
        "requests",
        "pydantic",
        "Click",        
    ]
)
```

In this case we are installing a main module `myproject` and all the packages found in the project directory.

This also installs the dependencies `requests`, `pydantic`, and `Click`.

### Defining entry points

You can define entry points for your project by using the `entry_points` argument in the `setup()` function.

```Python
from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    py_modules=["myproject"],
    packages=find_packages(),
    install_requires=[
        "requests",
        "pydantic",
        "Click",        
    ],
    entry_points={
        "console_scripts": [
            "mycommand=myproject:main",
        ]
    }
)
```

In this case, we are defining a console script `mycommand` that will run the `main` function in the `myproject` module.


The console_scripts metadata is used by setuptools to automatically create command line executables for us. 

The format is a dictionary where the key is the name of the command we want to create and the value is the module 
and function we want to run when the command is executed.

We can create multiple command line executables by adding more entries to the dictionary.

```Python
entry_points={
    "console_scripts": [
        "mycommand=myproject:main",
        "myothercommand=myproject:other",
    ]
}
```


## Installation

To install Setuptools, you can use the `pip` command:

```Shell
pip install setuptools
```


## Usage

To install your project, you can use the `pip` command:

```Shell
pip install .
```

This will install your project and its dependencies.


To install your project in editable mode, you can use the `-e` option:

```Shell
pip install -e .
```

or in the long format

```Shell
pip install --editable .
```

This will install your project in editable mode, which means that any changes you make to the project will be 
reflected in the installed version.

The pip install will install a command-line executable(s) into the ```venv/bin``` directory that will run the main
function in the module specified in the entry_points metadata.


## References

- [Python Packaging User Guide](https://packaging.python.org)
- [Setuptools Documentation](https://setuptools.pypa.io)