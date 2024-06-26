# GitHub

This document contains my personal notes on GitHub.

## Overview

GitHub is a web-based hosting service for version control using Git.  It is mostly used for computer code.  It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features.  It provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.


### Adding a local repo to GitHub with the GitHub CLI

You may need to login to your GitHub account using the gitHub CLI if you haven't already

```bash
gh auth login
```

> gh repo create project-name

If you want your project to belong to an organization instead of your user account specify the organization name and project name 

> gh repo create --source=. --public --remote=jedi-knights/project-name --push

> gh repo create --source=. --private --remote=jedi-knights/project-name --push

> gh repo create --source=. --internal --remote=jedi-knights/project-name --push

Note: this should be added to scaffit so that it automates the creation process even further

## References

- [GitHub](https://github.com)
