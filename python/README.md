# Python Notes

I'm in the process of converting my Python notes from markdown to Marimo notebooks. This will allow me to 
run the code snippets in the browser and make the notes more interactive.

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

To get started with the intro tutorial:

```shell
marimo tutorial intro
```

This will start the intro tutorial in the default browser.

### Usage

### Creating a new notebook

```shell
marimo edit
```

### Viewing the notebook

```shell
marimo run python/notebooks/marimo.md
```

## References

- [Python - Official Site](https://www.python.org/)
- [Marimo - Official Site](https://marimo.io/)
