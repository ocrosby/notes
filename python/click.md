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

## Function docstrings in the help page

Click automatically generates help pages for commands based on the docstrings of the functions. You can add docstrings to your functions to provide additional information about the command.

```Python
import click

@click.command()
def hello():
    """Prints a greeting message."""
    click.echo("Hello, World!")
    
if __name__ == "__main__":
    hello()
```

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS]

  Prints a greeting message.
  
Options:
    --help  Show this message and exit.
```

Note: Here the function docstring for the hello function gets rendered in the help page.

There is also a help argument to option that can be added to the option and arg to display in the help page.

```Python
import click

@click.command()
@click.option("--name", help="The name to greet.")
def hello(name):
    """Prints a greeting message."""
    click.echo(f"Hello, {name}!")
    
if __name__ == "__main__":
    hello()
```

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS]

  Prints a greeting message.
  
Options:
    --name TEXT  The name to greet.
    --help       Show this message and exit.    
```


### Defining multiple options

You can define multiple options for a command by using the `@click.option()` decorator multiple times.

```Python
# hello.py

import click

@click.command()
@click.option("--string", default="World", help="This is the thing that is greeted.")
@click.option("--repeat", default=1, help="How many times to greet the thing.")
def hello(string, repeat):
   """This script greets you."""
   for _ in range(repeat):
      click.echo(f"Hello, {string}!")
      
if __name__ == "__main__":
    hello()
```

Note: click automatically determines the type of the option based on the default value provided. In this case, 
the `--repeat` option is an integer because the default value is an integer.

In the option specification you can also be explicit by including the type of the option.

```Python
@click.option("--repeat", default=1, type=int, help="How many times to greet the thing.")
```
    
When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```


### Option name to argument mapping

By default, Click will map the option name to the argument name by replacing dashes with underscores.

```Python
import click

@click.command()
@click.option("--name", default="World", help="The name to greet.")
@click.option('--birth-date', default='2022-01-01', help='The birth date of the person.')
def hello(name, birth_date):
    click.echo(f"Hello, {name}! Your birth date is {birth_date}.")
    
if __name__ == "__main__":
    hello()
```

Notice here that the `--birth-date` option is mapped to the `birth_date` argument in the function.

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS]

Options:
    --name TEXT        The name to greet.
    --birth-date TEXT  The birth date of the person.
    --help             Show this message and exit.
```

### Arguments vs Options

Arguments are positional and options are not. Arguments are required by default, while options are not.

```Python
import click

@click.command()
@click.option("--greeting", default="Hello", help="The greeting message.")
@click.argument("name")
def hello(name, greeting):
    click.echo(f"{greeting}, {name}!")
    
if __name__ == "__main__":
    hello()
```

In this example, the `name` argument is required, while the `greeting` option is not.

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS] NAME

Options:
    --greeting TEXT  The greeting message.
    --help           Show this message and exit.
```

Note: Arguments come after options in the command line.

### Creating an output file argument

You can create an argument that takes a file path as input by using the `click.File()` function.

```Python
import click

@click.command()
@click.argument("output", type=click.File("w"))
def hello(output):
    output.write("Hello, World!")
    
if __name__ == "__main__":
    hello()
```

In this example, the `output` argument takes a file path as input and opens the file in write mode.


If you specify '-' as the output argument, Click will use stdin/stdout.

You can set the default to '-' to use stdin/stdout as the default.

```Python
import click

@click.command()
@click.argument("output", type=click.File("w"), default="-", required=False)
def hello(output):
    click.echo("Hello, World!", file=output)
    
if __name__ == "__main__":
    hello()
```

But when you do notice you will need to specify the required option argument as well.  This is because arguments
are positional and required by default.
   

Note: Arguments cannot have help text and should be documented as part of the docstring.

Using the specified output file:

```Shell
python hello.py output.txt
```

Note: These files open lazy by default, so unless you start writing to them they won't be opened.


### Using a subcommand

You can create a subcommand by using the `@click.command()` decorator on a function and adding it to the main command using the `@click.group()` decorator.

```Python
import click

@click.group()
@click.option('--verbose', is_flag=True
def cli(verbose):
    if verbose == True:
        click.echo('Verbose mode enabled.')
    else:
        click.echo('Verbose mode disabled.')
    
@cli.command()
def hello():
    click.echo("Hello, World!")
    
```


### Communicating with click Context


You can communicate with the click context by using the `click.get_current_context()` function.

```Python
import click

class Config(object):
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

# ensure=True will create a new instance of the object if it doesn't exist on the first use of @pass_config

@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home_directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    
    if home_directory is None:
        directory = '.'
        
    config.home_directory = directory   
    
@cli.command()
@click.option('--string', default='World', help='This is the thing that is greeted.')
@click.option('--repeat', default=1, help='How many times to greet the thing.')
@click.argument('out', type=click.File('w'), default='-', required=False)
@pass_config
def say(config, string, repeat, out):
    if config.verbose:
      click.echo('We are in verbose mode')
      
    click.echo('Home directory is %s' % config.home_directory)  
    for x in range(repeate):
      click.echo('Hello %s!' % string, file=out)
```

In this example, the `Config` class is used to store the configuration settings for the command. The `pass_config` decorator is used to pass the `Config` object to the command functions.

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS] COMMAND [ARGS]...

Options:
    --verbose
    --home_directory TEXT
    --help                  Show this message and exit.
    
Commands:
    say
```
   
   

### Using a click.Path option to specify a directory

You can create an option that takes a directory path as input by using the `click.Path()` function with the `file_okay=False` parameter.

```Python
import click

class Config(object):
    def __init__(self):
        self.verbose = False
        self.home_directory = None

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.command()
@click.option("--home_directory", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@pass_config
def hello(config, home_directory):
    if home_directory is None:
      directory = '.'
      
    config.home_directory = directory  
    click.echo(f"Directory: {directory}")
    
```

 


When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS] OUTPUT

Options:
    --help  Show this message and exit.
```

### Creating a password option

You can create an option that takes a password as input by using the `click.prompt()` function with the `hide_input=True` parameter.

```Python
import click

@click.command()
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
def hello(password):
    click.echo(f"Password: {password}")
    
if __name__ == "__main__":
    hello()
```

In this example, the `password` option takes a password as input and hides the input from the user.

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS]

Options:
    --password TEXT  [required]
    --help           Show this message and exit.
```

### Creating a choice option

You can create an option that takes a choice as input by using the `click.option()` decorator with the `type` parameter set to `click.Choice()`.

```Python
import click

@click.command()
@click.option("--color", type=click.Choice(["red", "green", "blue"]))
def hello(color):
    click.echo(f"Color: {color}")
    
if __name__ == "__main__":
    hello()
```

In this example, the `color` option takes a choice of `red`, `green`, or `blue` as input.

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS]

Options:
    --color [red|green|blue]
    --help  Show this message and exit.
```

### Creating a flag option

You can create an option that acts as a flag by using the `click.option()` decorator with the `is_flag` parameter set to `True`.

```Python
import click

@click.command()
@click.option("--verbose", is_flag=True)
def hello(verbose):
    if verbose:
        click.echo("Verbose mode enabled.")
    else:
        click.echo("Verbose mode disabled.")
        
if __name__ == "__main__":
    hello()
```

In this example, the `verbose` option acts as a flag that can be used to enable or disable verbose mode.

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS]

Options:
    --verbose
    --help     Show this message and exit.
```

### Creating a hidden option

You can create an option that is hidden from the help page by using the `click.option()` decorator with the `hidden` parameter set to `True`.

```Python
import click

@click.command()
@click.option("--hidden", hidden=True)
def hello(hidden):
    click.echo(f"Hidden: {hidden}")
    
if __name__ == "__main__":
    hello()
```

In this example, the `hidden` option is hidden from the help page.

When you run the command with the `--help` option, you will see the docstring displayed in the help page.

```Shell
python hello.py --help
```

This will output:

```Shell
Usage: hello.py [OPTIONS]

Options:
    --help  Show this message and exit.
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
