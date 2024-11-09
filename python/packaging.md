# Packaging

## What's the scoop with setup.cfg, setup.py, and pyproject.toml?

- setup.cfg is a configuration file for setuptools
- setup.py is a script that runs setuptools
- pyproject.toml is a configuration file for build tools

Two methods for creating a python package:

Method #1: Using `python setup.py`

Method #2: Using `pyproject.toml`

Install setuptools

```shell
pip install setuptools
```

Install your the package in editable mode

```shell
pip install --editable .
```

setup.py

```python
from setuptools import setup

setup(
    name='mycalculator',
    version='0.0.1',
    py_modules=['mycalculator'],
    packages=find_packages(),
    install_requires=[
        'requests',
        'pydantic',
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'calc=mycalculator:main',
        ]
    }
)
```

## Overview

Python packaging can be a bit confusing at first. There are many tools and standards to choose from.


Questions:

- What is the difference between a package and a module?
- What is the difference between a package and a distribution?
- What is the difference between a source distribution and a binary distribution?
- What is the difference between a wheel distribution and a source distribution?
- What is the difference between a universal distribution and a platform-specific distribution?
- How do you create a wheel package for your project?
- How do you create a source distribution for your project?
- How do you create a binary distribution for your project?
- How do you create a universal distribution for your project?
- How do you create a platform-specific distribution for your project?
- How do you create a pure Python distribution for your project?
- How do you create a C extension distribution for your project?

Note: An interesting article on the subject is [Python Packaging: A Brief Introduction](https://realpython.com/python-packaging/)

Python has a way to run a directory as a script. This is done by creating a `__main__.py` file in the directory. 
This is useful for creating command line tools.

Now we use pyproject.toml, it contains information about the project.

[Configuring Python Projects with pyproject.toml](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)

```toml

```python

## Using setup.py


Create a directory called hello_world

```bash
mkdir hello-world
cd hello-world
mkdir hello_world
touch hello_world/main.py
touch setup.py
mkdir tests
touch tests/test_foo.py
touch tests/__init__.py
```

Add the following code to hello_world/main.py

```python
def main():
    print("Hello, World!")
    
if __name__ == "__main__":
    exit(main())    
```

Add the following code to setup.py

```python
from setuptools import setup
from setuptools import find_packages

# Find packages looks over the directories and finds the packages
# packages are directories that contain an __init__.py file

setup(
    name='hello_world',
    version='1.0.0',
    description='A simple hello world program',
    author='Omar Crosby',
    author_email='omar.crosby@gmail.com',
    url='https://github.com/ocrosby/hello-world',
    packages=find_packages(exclude=['tests*']),  # exclude test packages
    py_modules=['main'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'hello=hello_world.main:main',  # hello is the command that will be created
        ]
    },
)
```

Note: You can use find_packages directly to see what it would return in an interactive shell.

```python
from setuptools import find_packages

# this one finds all packages
find_packages()

# this one finds all packages excluding tests and testing
find_packages(exclude=('tests*', 'testing*'))
```

## Using a Declarative Setup

First see [setup-py-upgrade](https://github.com/asottile/setup-py-upgrade)

If you have previously created a setup.py file as we did above

You can use setup-py-upgrade to convert your setup.py file into a declarative setup.cfg file

```bash
pip install setup-py-upgrade
cd hello-world
setup-py-upgrade .
```

This will create a setup.cfg file that looks like this:

```ini
[metadata]
name = hello_world
version = 1.0.0
description = A simple hello world program
author = Omar Crosby
author_email =
url =
classifiers =
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent
long_description = file: README.md
long_description_content_type = text/markdown
license = MIT
license_file = LICENSE
keywords =
    hello
    world
    example
```

Note: It should also have the entry points defined as well.

With this information in setup.cfg your setup.py file can be as simple as this:

```python
from setuptools import setup
setup()
```

Note: If you are using pyproject.toml you may be able to skip the setup.py file altogether.

## Why use the declarative setup.cfg file?

- It's easier to read
- It's easier to maintain
- It's easier to extend
- It's easier to share
- It's easier to programmatically generate and manipulate


```shell
pip install setup-cfg-fmt
setup-cfg-fmt setup.cfg
```

this will format the setup.cfg file

## References

- [How to Build a Complete Python Package Step-by-Step](https://www.youtube.com/watch?v=5KEObONUkik)