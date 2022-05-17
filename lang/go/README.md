# Go

## References

* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
* [Go Tooling](https://alexedwards.net/blog/an-overview-of-go-tooling)
* [Mage](https://magefile.org)
* [Project Layout](https://github.com/golang-standards/project-layout)

## Go Tooling

### Viewing Environment Information 

Displaying information about your current Go operating environment:

```bash
> go env
```

Displaying specific values from the Go operating environment:

```bash
> go env GOPATH GOOS GOARCH
```

Show documentation for all go env variables:

```bash
> go help environment
```

### Development

#### Running Code

During development the go run tool is a convenient way to try out your code.  It's essentially a shortcut that compiles your code, creates an executable binary in your /tmp directory, and then runs this binary in one step.

```bash
> go run .         # Run the package in the current directory
> go run ./cmd/foo # Run the package in the ./cmd/foo directory
```

#### Fetching Dependencies

If you have go modules enabled, when you use go run (or go test or go build) any external dependencies will automatically (and recursively) be downloaded to fulfill the import statements in your code.  By default the latest tagged release of the dependency will be downloaded, or if no tagged releases are available, then the dependency at the latest commit.

If you know in advance that you need a specific version of a dependency (instead of the one that Go would fetch by default) you can use `go get` with the relevant version number or commit hash.  For example

```bash
> go get github.com/foo/bar@v1.2.3
> go get github.com/fo/bar@8e1b8d3
```

#### Refactoring Code

#### Viewing Go Documentation

### Testing

#### Running Tests

Run all tests in the current directory.

```bash
> go test .
```

Run all tests in the current directory and sub-directories

```bash
> go test ./...
```

Run all tests in the ./foo/bar directory

```bash
> go test ./foo/bar
```

#### Profiling Test Coverage

You can enable coverage analysis when running tests by using the `-cover` flag.  This will display the percentage of code covered by the tests in the output for each package.

```bash
> go test -cover ./...
```

You can also generate a coverage profile using the -coverprofile flag and view it in your web browser by using the `go tool cover -html` command:

```bash
> go test -coverprofile=/tmp/profile.out ./...
> go tool cover -html=/tmp/profile.out
```

This gives you a navigable listing of all the tst files, with code covered by the tests displayed in green, and uncovered in code in red.

If you want you can go a step further and set the `-covermode=count` flag to make the profile record the exact number of times that each statement is executed during the tests.

```bash
> go test -covermode=count -coverprofile=/tmp/profile.out ./...
> go tool cover -html=/tmp/profile.out
```

When viewed in the browser, statements which are executed more frequently are shown in a more saturated shade a green.

Note: If you are using the `t.Parrallel()` command in any of your tests, then you should use the flag `-covermode=atomic` instead of `covermode=count` instead to insure an accurate count.

#### Stress Testing

You can use the `go test -count` command to run a test multiple times in succession, which can be useful if you want to check for sporadic or intermittent failures

```bash
> go test -run=^TestFooBar$ -count=500 .
```

The test will be repeated in serial - even if it contains a `t.Parallel()` instruction.  

I you want to use the `stress` tool to repeat the same test multiple times in parallel instead:

```bash
cd /tmp
GO111MODULE=on go get golang.org/x/tools/cmd/stress
```

To use the stress tool, you'll first need to compile a test binary for the specific package you want to test.  You can do that using the `go test -c` command.

```bash
> go test -c -o/tmp/foot.test .
```

The test binary will be outputted to /tmp/foo.test.  You can then use the stress tool to execute a specific test in the test binary:

```bash
> stress -p=4 /tmp/foo.test -test.run=^TestFooBar$
```

This restricts the number of parallel processes used to 4.  Without this flag, the tool will default to using a number of processes equal to `runtime.NumCPU()`.
#### Testing all Dependencies

Run tests on all packages in your module and all dependencies - include testing dependencies and the necessary standard library packages.  It can help validate that the exact versions of the dependencies being used are compatible with each other. (Can take a long time)

```bash
> go test all
```


### Pre-Commit Checks

#### Formatting Code

Go provides two tools to automatically format your code according to go conventions: `gofmt' and `go fmt`.  Using these helps keep your code consistent across your files and projects, and - if you use them before committing code - helps reduce noise when examining a diff between file versions.

Format the foo.go file

```bash
> gofmt -w -s -d foo.go
```

Recursively format all files in the current directory and sub-directories

```bash
> gofmt -w -s -d .
```

In these commands the `-w` flag instructs the tool to rewrite files in place, the `-s` instructs the tool to apply simplifications to the code where possible, and the `-d` flag instructs the tool to output diffs of the changes.  If you want to only display the names of the changed files, instead of diffs, you can swap this for the `-l` flag instead.

Note: `gofmt` is a wrapper which essentially calls `gofmt -l -w` on a specified file or directory.

```bash
> go fmt ./...
```

#### Performing Syntax Analysis

The `go vet` tool carries out static analysis of your code and warns you of things which might be wrong with your code but wouldn't be picked up by the compiler.  Issues like unreachable code, unecessary assignments and badly-formed build tags.

Vet the foo.go file

```bash
> go vet foo.go
```

Vet all files in the current directory 

```bash
> go vet .
```

Vet all files in the current directory and sub-directories

```bash
> go vet ./...
```

Vet all files in the ./foo/bar directory

```bash
> go vet ./foo/bar
```

Behind the scenes, `go vet` runs a bunch of different analyzers.

Disable the composite analyzer

```bash
> go vet -composites=false ./...
```



#### Linting Code

#### Tidying and Verifying your Dependencies

### Build and Deployment

#### Building an Executable

#### Cross-Compilation

#### Using Compiler and Linker Flags

### Diagnosing Problems and Making Optimizations

#### Running and Comparing Benchmarks

#### Profiling and Tracing

#### Checking for Race Conditions


### Managing Dependencies

### Upgrading to a New Go Release

### Reporting Bugs

### Cheatsheet

## Go Programming Language

Syntax of a function in Go

```go
func function_name([parameter list]) [return_types] {
    // body of the function
}
```

Four Categories of variables in Go

1. Boolean

There are two values true and false.  Bool is one of the four elementary types.

2. Numeric

These can be integers or floating-point values.  

Examples:

* uint8 (unsigned 8-bit integers from 0 to 255)
* int16 (signed 16-bit integers)
* float32
* float64
* complex62 (float32 with real and imaginary parts)
* complex128 (float64 with real and imaginary parts)
* Both int and float are elementary types

3. Strings

Once created, the string cannot be changed.
A string is also an elementary type.

1. Derived Types

These include pointer types, array types, structure types, map types, etc.

### Constants

Go doesn't allow you to mix numeric types.

Unless you explicitly give a constant a type, it's considered to be untyped, even if you give it a name.  An untyped constant that's an integer can only be used where integers are allowed.  An untyped floating-point constant can be used wherever a floating point is permitted.

All untyped constants in Go have default types.  Constants that are integers default to "int", floats default to "float64", characters to "rune", etc.  When you declare a type, the constant becomes typed.  Again, constants must be declared as their correct type, or else the program will return an error.

Declare constants without a type unless you absolutely need them;  declaring a type makes you lose flexibility of being able to mix types in an operation.

#### Rules for constant expressions in Go

* Comparison between two untyped constants results in an untyped boolean constant ("true"/"false").
* Operands of the same type result in the same type.  The expression "11/2" results in "5" rather than "5.5" because it's truncated to an integer.
* If they're not the same type, the result is the broader of the two according to this logic: "integer<rune<floating-point<complex"

### Variables

Names of variables can use letters, digits, and underscores.  Golang variables have a specific size, memory layout, range of values for the memory layout, and possible operations.  The variable definition tells the compiler how much storage to create for the variable and where to put it.

You use the var keyword to declare a variable.

### Three types of operators in Go.

#### Bitwise Operators

* AND: &
* OR: |
* XOR and COMPLEMENT: ^
* CLEAR: &^
* Arithmetic

#### Arithmetic Operators

* +, Addition
* *, Multiplication
* /, Division
* %, Percentage

#### Logical Operators

* Equal: =
* Not Equal: !=
* Less than: <
* Less than or equal to: <=
* Greater than: >
* Greater than or equal to: >=

### Strings

Strings are immutable, or read-only.  The characters represent bytes that are UTF-8 encoded.

```go
package main

import "fmt"

func main() {
    var my_words string

    my_words = "Hello World!"

    fmt.println("String: ", my_words)
}
```

### Times and Dates

In Go, times include a location that determines the date and time associated with that location.  If it's not specified, the time defaults to UTC.

If you want a timestamp, Time.Now: the signature is:

```go
func Now() time
```

For the date and time, Time.Date, the signature is in the format yyyy-mm-dd hh-mm-ss + nanoseconds:

```go
func Date (year int, month, day, hour, min, sec, nsec int, loc *Location)
```

In Go, the duration is what's elapsed in nanoseconds betweeen two instants written in int64nanosecond count.

```go
func Since(t Time) duration
```

If you want to know how long until time t, the function is:

```go
func Until(t Time) duration
```

### Control Structures

#### Conditionals

```go
package main

import(
    "fmt"
)

func main() {
    var grade = A

    x:= true

    if x {
        fmt.PrintLn(grade)
    }
}
```

```go
if condition {
    // code that will be executed if the condition is true
}
```

```go
if condition {
    // code that will be executed if the condition is true
} else {
    // code that will be executed if the condition is false
}
```

```go
if condition_1 {
    // code that will be executed if the condition_1 is true
} else if condition_2 {
    // code that will be executed if the condition_2 is true
} else {
    // code that will be executed if both conditions are false
}
```

```go
switch target {
    case case_1:
        // handle case_1
    case case_2, case_3:
        // handle cases 2/3
    default:
        // handle default case
}
```

Note: In Go, the control switch runs the first case where the condition is true and ignores the remainder.  So you don't have to explicitly break out.

#### Loops

```go
package main

import(
    "fmt"
)

func main() {
    for x:=1; x<= 10; x++ {
        fmt.PrintLn(x)
    }
}
```
