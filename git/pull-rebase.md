# Git Pull Rebase


Always try `git pull --rebase` instead of `git pull` to avoid merge commits.

This will pull the latest changes from the remote repository and reapply your local changes on top of them.

```bash
git pull --rebase
```

If you have a merge conflict, you will need to resolve it manually.

```bash
git status
```

Git status at this point will show you the conflicted files.

```bash
git diff
```

At this point, you can edit the conflicted files to resolve the conflict.

```bash
git add <file>
```

After you have resolved the conflict, you can continue the rebase.

```bash
git rebase --continue
```

If you want to skip the commit that caused the conflict:

```bash
git rebase --skip
```

If you gert a conflict and want to abort the rebase:

```bash
git rebase --abort
```

## References

- [Never* use git pull - Video](https://www.youtube.com/watch?v=xN1-2p06Urc)