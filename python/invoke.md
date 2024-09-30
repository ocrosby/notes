# Using Invoke in Python Projects

Invoke is a Python task execution tool and library that allows you to define and run tasks from the command line. It is often used for automating repetitive tasks in development workflows.

## Installation

To install Invoke, use pip:

```shell
pip install invoke
```

## Defining Tasks

Tasks in Invoke are defined using Python functions and the @task decorator. These tasks can then be executed from the command line.  

### Example

Create a file named tasks.py and define some tasks:

```python
from invoke import task

@task
def clean(c):
    """Clean up build artifacts."""
    c.run("rm -rf build dist *.egg-info")

@task
def build(c):
    """Build the project."""
    c.run("python setup.py sdist bdist_wheel")

@task
def test(c):
    """Run tests."""
    c.run("pytest")
```

## Running Tasks

To run a task, use the invoke command followed by the task name. For example, to run the clean task:

```shell
invoke clean
invoke build
invoke test
```

or using the short form:

```shell
inv clean
inv build
inv test
```

You can also pass arguments to tasks:

```python
@task
def greet(c, name):
    """Greet a person by name."""
    print(f"Hello, {name}!")
```

```shell
inv greet --name Alice
```

## Task Dependencies

You can define task dependencies by calling other tasks from within a task:

```python
@task(pre=[clean])
def build(c):
    """Build the project."""
    c.run("python setup.py sdist bdist_wheel")
```

In this example, the build task depends on the clean task, so clean will be executed before build.

## Namespaces

You can organize tasks into namespaces to group related tasks together:

```python
from invoke import Collection

@task
def task1(c):
    print("Task 1")
    
@task
def task2(c):
    print("Task 2")

ns = Collection(clean, build, test)
ns.add_task(task1)
ns.add_task(task2)
```


## References

- [Invoke Documentation](http://docs.pyinvoke.org/en/stable/)
- [Invoke GitHub Repository](https://github.com/pyinvoke/invoke)