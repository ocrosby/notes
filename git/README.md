# Git

Initialize a new local git repository

```shell
git init
```


Add the remote repository URL from a local repository to GitHub

```shell
git remote add origin <remote_repository_url>
```

Verify the remote URL

```shell
git remote -v
```

Push your changes to the remote repository

```
git push -u origin main
```


Checkout a repository

> git clone https://github.com/yourname/yourrepo.git

This would checkout yourrepo into a directory called yourrepo in the current directory.

Show which branches are available

> git branch

Creating a new branch
> git branch feature/new-branch

Switching to a new branch
> git checkout feature/new-branch

Checkout/Create a new local branch
> git checkout -b experimental-branch


Stage a file (get ready to commit)
> git add readme.txt


Display the status
> git status


> git commit -m "updated the readme"



> get checkout master


> get merge experimental-branch

> git status

> get log


Deleting a local branch
> git branch --delete <branchname>


## Resolving Simple Merge Conflicts in Git

Check out the branch you want to check in to first.  So if there is a merge conflict with develop and you are on feature/your-feature.

> git checkout feature/your-feature
> git merge develop


If you wanted to abort the merge then

> git merge abort

Save the file with the changes you are happy with.

> git status

Will show that the file is not resolved.

> git add content.txt
> git commit -m "merged his branch"
> git status

should be happy

## Removing Something from Version Control Without Deleting It

From time to time I will accidentally commit something like my .idea directory that I don't want in my repo.  In order to remove it from verison control without deleteing the file simply do the following.

```bash
git rm -r --cached .idea
git commit -m "untrack .idea directory"
git push
```

## Worktrees

You can now use the `git worktree` command to create a new worktree.  This is useful if you want to work on a new feature or bug fix without having to switch branches.

```bash
git worktree add -b new-feature ../new-feature
```

This will create a new branch called new-feature and create a new directory called new-feature in the parent directory of the current directory.

It also apparently creates a link back to the main worktree's .git directory so that you can commit changes from the new worktree.

This practice allows you to work on multiple branches at the same time.