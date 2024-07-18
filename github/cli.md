# GitHub CLI

## Usage

Getting help for a particular command

```Shell
gh repo create help
```

Creating a new repository from the command line

```Shell
gh repo create example-repo --private --description "This is an example repository"
```

```Text
gh repo create help
`--public`, `--private`, or `--internal` required when not running interactively

Usage:  gh repo create [<name>] [flags]

Flags:
      --add-readme             Add a README file to the new repository
  -c, --clone                  Clone the new repository to the current directory
  -d, --description string     Description of the repository
      --disable-issues         Disable issues in the new repository
      --disable-wiki           Disable wiki in the new repository
  -g, --gitignore string       Specify a gitignore template for the repository
  -h, --homepage URL           Repository home page URL
      --include-all-branches   Include all branches from template repository
      --internal               Make the new repository internal
  -l, --license string         Specify an Open Source License for the repository
      --private                Make the new repository private
      --public                 Make the new repository public
      --push                   Push local commits to the new repository
  -r, --remote string          Specify remote name for the new repository
  -s, --source string          Specify path to local repository to use as source
  -t, --team name              The name of the organization team to be granted access
  -p, --template repository    Make the new repository based on a template repository
```

Adding a new remote to an existing repository

```Shell
git remote add origin https://github.com/username/repo.git
```

Adding something to the ignore list from the command-line

```Shell
echo "file.txt" >> .gitignore
```

Adding a new remote

```Shell
git remote add main https://github.com/username/repo.git
```


Pushing a new repository to GitHub

```Shell
git push --set-upstream main main
```

