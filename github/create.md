# Creating a GitHub repo from the terminal

## Overview

To start development of new projects we routinely need to create new repositories.  
When working with developers who are new to GitHub it can be helpful to show them how 
to create a new repository from the terminal to speed up their process.

This guide will walk you through the process of creating a new GitHub repository directly 
from your terminal using the GitHub CLI (gh).

## Prerequisites

Before you begin, ensure that you have the GitHub CLI (gh) installed and authenticated with your GitHub account.

### Installing GitHub CLI

1. **Download and Install GitHub CLI**

   You can download and install the GitHub CLI from the GitHub CLI repository on GitHub. Follow the installation instructions appropriate for your operating system:

    - **macOS**:

      ```bash
      brew install gh
      ```

    - **Windows**:

      Download the GitHub CLI installer from [GitHub Releases](https://github.com/cli/cli/releases) and follow the installation instructions.

    - **Linux**:

      You can find installation instructions for various Linux distributions in the [GitHub CLI documentation](https://cli.github.com/manual/installation).

2. **Log In to Your GitHub Account**

   After successfully installing the GitHub CLI, you'll need to log in to your GitHub account using the following command:

   ```bash
   gh auth login
   ```
   
    Follow the prompts to authenticate with your GitHub account.


## Steps
1. Create a New GitHub Repository

    ```shell
    mkdir my-new-repo
    cd my-new-repo
    git init
    ```

    To create a new GitHub repository, use the gh repo create command. Replace <repository_name> with the name you want for your new repository:

    ```bash
    gh repo create <repository_name> --public --source=. --remote=origin
    ```
   
This command will create a new public repository with the specified name and set the current directory as the source. It will also add a remote named origin to the repository.

you can use the --public or --private flags to set the repository's visibility
the --source option points to the current directory
the --remote option automatically sets the origin remote


2. Configure Repository Settings

    After running the command, the GitHub CLI will prompt you to configure various settings for your new repository. You can set options like the repository's visibility (public or private) and whether to initialize it with a README, license, or .gitignore file.

3. Access Your New Repository

    Once the configuration is complete, the GitHub CLI will create the new repository on your GitHub account. It will provide you with the URL of the newly created repository.

4. Manage Your Repository

    You can now manage your new GitHub repository directly from the terminal, including pushing code to it, managing issues, and collaborating with others.

That's it! You've successfully created a new GitHub repository from the terminal using the GitHub CLI.



## Creating a React App and Adding it to GitHub

This assumes you have already logged in to GitHub using the GitHub CLI (gh) as detailed above.

```bash
npx create-react-app react-seed
cd react-seed
gh repo create --source=. --public --remote=<github-username>/react-seed --push
git remote add origin https://github.com/<github-username>/react-seed.git
```

Note: create-react-app initializes a git repo for you, so you will have a .git directory available in the 
react-seed directory.

In this example you would need to replace github-username with your GitHub username (removing the brackets).

So if your GitHub username is jdoe for example it would look like this:

```bash
npx create-react-app react-seed
cd react-seed
gh repo create --source=. --public --remote=jdoe/react-seed --push
git remote add origin https://github.com/jdoe/react-seed.git
```

## References 

- [GitHub CLI](https://cli.github.com/)