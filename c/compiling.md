# Compiling C Code

This document contains my personal notes on compiling C code.

## Overview

The following is a list of commands that can be used to compile C code:

```sh
gcc -o hello hello.c
```

```sh
gcc -o hello hello.c -Wall
```

```sh
gcc -o hello hello.c -Wall -Werror
```

```sh
gcc -o hello hello.c -Wall -Werror -std=c99
```

```sh
gcc -o hello hello.c -Wall -Werror -std=c99 -g
```

