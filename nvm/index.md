# Node Version Manager

## Overview

NVM stands for Node Version Manager.  It is a tool for managing multiple versions of 
node on a single machine.  This is useful for testing applications with different
versions of node.

## Installation

Installing nvm:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```

## Usage

Listing remote versions:

```bash
nvm ls-remote
```

Installing a specific version of node:

```bash
nvm install 14.17.0
```

Listing local versions:

```bash
nvm ls
```

Switching to a specific version:

```bash
nvm use 14.17.0
```

Specifying the default version:

```bash
nvm alias default 14.17.0
```

## References

