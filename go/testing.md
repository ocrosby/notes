# Testing in Go

A test in go is writen like this:

```go
// Path: hello.go
package main

import "fmt"

func Hello() string {
    return "Hello, world"
}

func main() {
    fmt.Println(Hello())
}
```

```go
// Path: ./hello_test.go
package main

import "testing"

func TestSomething(t *testing.T) {
    got := Hello()
    want := "Hello, world"

    if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
```


To run the test, you can use the `go test` command:

```Shell
go test
```

As long as you have initialized your module with `go mod init`, you can run the test from the root of your project.


## Writing Tests

- Tests should be in a file with a name like `xxx_test.go`
- The test function must start with the word `Test`
- The test function takes one argument only `t *testing.T`
- To use the `t.Error` or `t.Fail` you need to import the `testing` package

`t` of type `*testing.T` is our "hook" into the testing framework. 

Forcing a failure is as simple as calling `t.Fail()` or `t.Error()`.


## Running Tests

- Run your tests with `go test`
- Use the `-v` flag to see the output of the tests
- Use the `-run` flag to run a specific test

```Shell
go test -v
```

```Shell
go test -run TestSomething
```

## Benchmarking

To write a benchmark, you need to create a file with the `_test.go` suffix and a function that starts with `Benchmark`.

```go
func BenchmarkHello(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Hello()
    }
}
```

To run the benchmark, you can use the `go test` command with the `-bench` flag:

```Shell
go test -bench .
```

The `-bench` flag will run the benchmark function in the test file.

The output of the benchmark will show you the number of operations per second and the time it took to run the benchmark.

