# Click

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code 
as necessary. It is a simple and easy-to-use library that can be used to build complex command line applications.

## Overview

- arbitrary nesting of commands
- atomic help page generation
- supports lazy loading of subcommands at runtime

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
    - [Basic Command](#basic-command)
    - [Command with Arguments](#command-with-arguments)
    - [Command with Options](#command-with-options)
    - [Grouping Commands](#grouping-commands)
3. [Click Project Structure](#click-project-structure)
4. [References](#references)

## Installation

```Shell
pip install click
```

## Usage

Initially when working on a click project it's best to start off by creating your main module like this

```Python
def cli():
   print 'Hello World!'
```

So you can test the setuptools installation without click first.

```Python
from setuptools import setup

setup(
    name='myproject',
    version='0.1',
    py_modules=['myproject'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        myproject=myproject:cli
    ''',
)
```

Then you can run the following command to install the package

```Shell
pip install -e .
```

Or using the long form:

```Shell
pip install --editable .
```

after this point you can run the command `myproject` in the terminal and it should print `Hello World!`

```Shell
myproject
```

This is made possible because the installation adds a command-line directory to your virtual environment's bin directory.

Once this is verified you can start by changing the `cli` function to use click.

```Python
import click

@click.command()
def cli():
    click.echo('Hello World!')
```

The difference here is that you can now use the help menu to see what the command does.

```Shell
myproject --help
```

This demonstrates click at work.


### Basic Command

To create a Click command, you need to use the `@click.command()` decorator.

```Python
import click

@click.command()
def hello():
    click.echo("Hello, World!")

if __name__ == "__main__":
    hello()
```

To run the command, you can use the `python` command:

```Shell
python hello.py
```

This will output:

```Shell
Hello, World!
```


### Command with Arguments

You can add arguments to a Click command by using the `@click.argument()` decorator.

```Python
import click

@click.command()
@click.argument("name")
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    hello()
```

To run the command with an argument, you can use the `python` command:

```Shell
python hello.py Alice
```

This will output:

```Shell
Hello, Alice!
```

### Command with Options

You can add options to a Click command by using the `@click.option()` decorator.

```Python
import click

@click.command()
@click.option("--name", default="World", help="The name to greet.")
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    hello()
```

To run the command with an option, you can use the `python` command:

```Shell
python hello.py --name=Alice
```

This will output:

```Shell
Hello, Alice!
```

### Grouping Commands

You can group commands together using the `@click.group()` decorator.

```Python
import click

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello, World!")

@cli.command()
@click.argument("name")
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    cli()
```

To run the commands, you can use the `python` command:

```Shell
python hello.py hello
```

This will output:

```Shell
Hello, World!
```

```Shell
python hello.py greet Alice
```

This will output:

```Shell
Hello, Alice!
```

## Generating output using click.echo

The `click.echo()` function is used to generate output in Click commands. It is similar to the `print()` function in Python but provides additional features such as formatting and color support.

```Python
import click

@click.command()
def hello():
    click.echo("Hello, World!")
    
if __name__ == "__main__":   
    hello()
```


## Click Project Structure

```text
my_cli/
├── my_cli/
│   ├── __init__.py
│   ├── cli.py  # Main entry point for the CLI
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── command1.py  # First subcommand
│   │   ├── command2.py  # Second subcommand
│   │   └── ...          # Additional subcommands
├── tests/
│   ├── __init__.py
│   ├── test_command1.py  # Tests for the first subcommand
│   ├── test_command2.py  # Tests for the second subcommand
│   └── ...               # Additional tests
├── setup.py              # Setup script for the package
└── README.md             # Project README
```

## References

- [Click - Python Documentation](https://click.palletsprojects.com)
- [Click - PyPI](https://pypi.org/project/click/)
