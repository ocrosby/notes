# Automating Versioning with Semantic Release

Often in software development, we need to keep track of the versions of our software. This is important for a number 
of reasons, including:

- Keeping track of what changes have been made to the software
- Communicating changes to users
- Ensuring that users are using the latest version of the software
- Ensuring that users are using the correct version of the software

One way to automate versioning is to use a tool called Semantic Release. Semantic Release is a tool that automates 
the process of versioning your software based on the content of your commits. It uses 
the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification to determine the type of 
changes that have been made to the software, and then automatically increments the version number based on those 
changes.

## Installation

To install Semantic Release, you can use the following command:

```bash
pip install python-semantic-release
```

## Configuration

To configure Semantic Release, you need to create a `release.config.js` file in the root of your project. This file
should contain the following configuration:

```toml
[tool.semantic_release]
version_toml = [
    "pyproject.toml:project.version",
]
branch = "main"
upload_to_repository = false
upload_to_release = true
build_command = "pip install invoke && invoke build"
version_source = "tag"
commit_version_number = true
commit_message = "chore(release): v{version} [skip ci]"
```


From the docs:

- Update changelog file - CHAGNELOG.md by default
- Run semantic-release version - anlyzes the commit history to calculate semver tag
- Push changes to git - updated pyporject.toml and CHANGELOG.md
- Run build_command and upload the distribution file to your repository - we skip this upload
- Attach the files created by build_command to a new, tagged GitHub release

## Usage

To use Semantic Release, you need to follow the Conventional Commits specification when writing your commit messages.

Here are some examples of valid commit messages:

```bash
feat: add new feature
fix: fix bug
docs: update documentation
style: format code
refactor: refactor code
test: add tests
chore: update dependencies
```

Once you have written your commit messages, you can run the following command to release a new version of your software:

```bash
semantic-release publish
```

This command will analyze the commit history of your project, determine the type of changes that have been made, and 
then automatically increment the version number of your software based on those changes.

## Conclusion

Semantic Release is a powerful tool that can help you automate the process of versioning your software. By following
the Conventional Commits specification and using Semantic Release, you can ensure that your software is always
versioned correctly and that your users are always using the latest version of your software.

## References

- [Commitizen to enforce conventional commits](https://guicommits.com/commitizen-to-enforce-conventional-commits/)
- [Conventional Commits with Commitizen](https://guicommits.com/conventional-commits-with-commitizen/)
- [Conventional Commits with Husky](https://guicommits.com/conventional-commits-with-husky/)
- [Commitlint](https://commitlint.js.org/)
- [Semantic Release to automate publishing to Pypi](https://guicommits.com/semantic-release-to-automate-versioning-and-publishing-to-pypi-with-github-actions/)
- [Python Semantic Release](https://python-semantic-release.readthedocs.io/)
- [Semantic Release](https://semantic-release.gitbook.io/semantic-release/)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Semantic Versioning](https://semver.org/)
