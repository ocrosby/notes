# ZSH

## Errors

### compinit: insecure directories, run compaudit for list.
I started getting this weird error when the shell started:

"zsh compinit: insecure directories, run compaudit for list.
Ignore insecure directories and continue [y] or abort compinit [n]? ncompinit: initialization aborted"

To fix this I commented out the line containing "bash_completion" and the one trying to autoload compinit.
I also placed a clear command at the bottom of the .zshrc file.