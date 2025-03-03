# Using Marimo Notebooks

This document contains my personal notes on Marimo Notebooks.

## Setup

### Install

Setup Marimo in a new Virtual environment
```shell
mkdir example
cd example
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install marimo

# Install a few commonly utilized dependencies
pip install -r requirements.txt
```

View the Help menu

```shell
marimo --help
```

View the tutorial list

```shell
marimo tutorial --help
```

## Recommended Tutorial Sequence

Marimo recommends the following tutorial sequence
for people new to the platform:

1. intro
2. dataflow
3. ui
4. markdown
5. sql
6. layout
7. fileformat
8. markdown-format
9. for-jupyter-users

To view the tutorial list

```shell
marimo tutorial --list
```

To get started with the intro tutorial:

```shell
marimo tutorial intro
```

This will start the intro tutorial in the default browser.

### Usage

Running the tutorial

```shell
marimo tutorial intro
```

### Creating a new notebook

```shell
marimo new python/notebooks/marimo.md
```

### Viewing the notebook

```shell
marimo view python/notebooks/marimo.md
```


## References

- [GitHub](https://github.com/marimo-team/marimo)
- [Documentation](https://docs.marimo.io/)
- 