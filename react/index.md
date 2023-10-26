# React

## Overview

This document contains my personal notes on React

The big deal about react is that it is Declarative instead of Imperative.  This means 
that you tell it what you want and it figures out how to do it.  This is in contrast 
to Imperative programming where you tell it how to do it.

### Creating a new local React project

```bash
npx create-react-app my-app
```

Delete the React project

```bash
rm -rf my-app
```

Note: You can also use another tool called vite to create a react project.
More information about vite can be found here: https://vitejs.dev/guide

### Starting the development server

```bash
cd my-app
npm run start
```

Quick Start in CodeSandbox

There is a really cool tool to help you get started with a skeleton React project
on CodeSandbox.  You can simply type react.new in the browser and it will spin up
a new minimal React environment for you to experiment.

Open a browser to react.new

Creating a new React environment in CodeSandbox on Linux from the command line

```bash
google-chrome --new-tab "https://react.new"
```

Creating a new React environment in CodeSandbox on Windows from the command line

```bash
start chrome "https://react.new"
```

Creating a new React environment in CodeSandbox on MacOS from the command line

```bash
open -na "Google Chrome" --args --new-tab "https://react.new"
```



React apps are made outo of components.  A component is a piece of the UI that has it's own logic and appearance.  A component can be as small as a button, or as large as an entire page.

React components are JavaScript functions that return markup:


An example react component

```text
function MyButton() {
	return (
		<button>I'm a button</button>
	);
}
```


Nesting a component into another component:

```text
export default function MyApp() {
	return (
		<div>
		  <h1>Welcome to my app</h1>
		  <MyButton />
		</div>
	);
}
```

Notice that <MyButton /> starts with a capital letter.  That's how you know it's a React component.  

React component names must always start with a captial letter, while HTML tags must be lowercase.


The export default keywords specify the main component in that file.


Most react projects use JSX for convenience.

Components can't return multiple JSX tags.  You have to wrap them into a shared parent, like a <div>...</div> or an empty <>...</> wrapper:


Example:

```text
function AboutPage() {
	return (
		<>
			<h1>About</h1>
			<p>Hello.<br />How do you do?</p>
		</>
	);
}
```

## References

- [Export Statements](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export)
- [Import/Export](https://javascript.info/import-export)
- [Creating a new react application](create_react_app.md)
- [Tools recommended for local development](https://react.dev/learn/installation)
























