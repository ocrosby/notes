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
3. [References](#references)

## Installation

```Shell
pip install click
```

## Usage

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
