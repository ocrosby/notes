# Managing Go Projects

## Introduction to Packages

- 2007 - Google started designs for Go
- 2009 - Go was announced to the public
- 2009 - Go was open sourced
- 2012 - Go 1.0 was released
- 2018 - Go 1.11 was released with modules

GOROOT is the installation directory

GOPATH is the workspace directory where your code will reside.


GOOROOT
- src
- pkg
- bin


GOPATH
- src
- pkg
- bin


On my system it appears GOROOT is /usr/local/Cellar/go/1.21.2/libexec.  There are some standard links that appear
to be used that point to this directory.

```shell
ls -l /usr/local/bin/go
lrwxr-xr-x  1 omarcrosby  admin  32 Oct  3  2020 /usr/local/bin/go -> ../Cellar/go/1.15.2/bin/go
```

```shell