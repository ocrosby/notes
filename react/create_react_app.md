# Creating a new React application

## Overview

This document contains my personal notes on creating a new React application.

Installing version 20.8.0 of node:

```sh
nvm install 20.8.0
```

Set the default version of node to 20.8.0:

```sh
nvm alias default 20.8.0
```

Switching to version 20.8.0 of node:

```sh
nvm use 20.8.0
```

Creating a new React app

```sh
echo y | npx create-react-app my-app
cd my-app
npm ci
```

Delete react app

```sh
rm -rf my-app
```

Start the development server:

```sh
cd my-app
npm run start
```

Displaying the current version of node:

```sh
node --version
```

Initializing a React app in the current directory:

```sh
npx create-react-app .
```

## References

- [Create React App](https://create-react-app.dev/docs/getting-started/)