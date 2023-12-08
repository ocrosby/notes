# Makefiles

## What is a Makefile?

A Makefile is a file that contains a set of instructions for the compiler to

## Example of a Makefile

```makefile
# Makefile for hello.c

hello: hello.c
    gcc -o hello hello.c -Wall -Werror -std=c99 -g
```

This Makefile contains a single rule that tells the compiler how to compile the `hello.c` file.

Assuming that there is a file named hello.c in the current directory executing the make command will compile the hello.c file and create an executable named hello.

Create a file named hello.c with the following contents:

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

Execute the make command:

```sh
make
```

The make command will compile the hello.c file and create an executable named hello.


# Multiple Source Files

## Example of a Makefile with Multiple Source Files



## References

* [Makefile Guide](http://www.cs.duke.edu/~ola/courses/programming/Makefiles/Makefiles.html)
* [Example of a Makefile](https://www.cse.scu.edu/~sfigueir/11/makefile)
