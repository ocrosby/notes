# Git

Show which branches are available


> git branch

Creating a new branch
> git branch feature/new-branch

Switching to a new branch
> git checkout feature/new-branch


Checkout/Create a new local branch
> git checkout -b experimental-branch


Stage a file
> git add readme.txt


show

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
