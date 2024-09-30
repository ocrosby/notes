# Using Git to change a previous commit

You can use `git commit --amend` to allow you to modify the most recent commit.  It's useful when you want to correct mistakes, add missing changes, or update the commit message.

## Basic Usage

To add changes to the last commit:

1. Stage your new or modified files:

```shell
git add <file>
```

2. Amend the last commit:

```shell
git commit --amend --no-edit
```

This would keep the commit message unchanged.  If you want to edit the message, omit the --no-edit flag.


**When to Use**

- Fixing a typeo in the commit message
- Adding missed changes.
- Updating metatdata (e.g., authorship).

## Push Changes

If you've already pushed, you'll need to force-push the amended commit:

```shell
git push --force
```

**Example**

```shell
git add package.json
git commit --amend --no-edit
git push --force
```

This command sequence restores files and updates the last commit.

## References
- [Add changes to previous commit - Article](https://graphite.dev/guides/add-changes-to-previous-commit)
