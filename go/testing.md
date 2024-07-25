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

## Subtests

Subtests allow you to group tests together. 

Let's say we expect this functionality:

```go
func TestHello(t *testing.T) {
	t.Run("saying hello to people", func(t *testing.T) {
		got := Hello("Chris")
		want := "Hello, Chris"

		if got != want {
			t.Errorf("got %q want %q", got, want)
		}
	})
	t.Run("say 'Hello, World' when an empty string is supplied", func(t *testing.T) {
		got := Hello("")
		want := "Hello, World"

		if got != want {
			t.Errorf("got %q want %q", got, want)
		}
	})
}
```

Here we have defined two subtests of the `TestHello` test.

We are assuming that the `Hello` function takes a string and returns a string.

```Go
func Hello(name string) string {
    if name == "" {
        name = "World"
    }
    return "Hello, " + name
}
```

Note that in this case we found it useful to group tests around a "thing" and then have subtests describing different scenarios.

A benefit of this approach is you can set up chared code that can be used in the other tests.

Refactoring the tests

```go
func TestHello(t *testing.T) {
	t.Run("saying hello to people", func(t *testing.T) {
		got := Hello("Chris")
		want := "Hello, Chris"
		assertCorrectMessage(t, got, want)
	})

	t.Run("empty string defaults to 'world'", func(t *testing.T) {
		got := Hello("")
		want := "Hello, World"
		assertCorrectMessage(t, got, want)
	})
}

func assertCorrectMessage(t testing.TB, got, want string) {
	t.Helper()
	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}
```

We've refactored our assertion into a new function. This reduces duplication and improves the readability of our tests. We need to pass in t *testing.T so that we can tell the test code to fail when we need to.

For helper functions, it's a good idea to accept a testing.TB which is an interface that *testing.T and *testing.B both satisfy, so you can call helper functions from a test, or a benchmark (don't worry if words like "interface" mean nothing to you right now, it will be covered later).

t.Helper() is needed to tell the test suite that this method is a helper. By doing this, when it fails, the line number reported will be in our function call rather than inside our test helper. This will help other developers track down problems more easily. If you still don't understand, comment it out, make a test fail and observe the test output. Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. You can comment out the t.Helper() code by adding two forward slashes // at the beginning of the line. You should see that line turn grey or change to another color than the rest of your code to indicate it's now commented out.

A new requriement came down that you needed to specify the language in the greeting. 

```go
func greetingPrefix(language string) (prefix string) {
    switch language {
    case "Spanish":
        prefix = "Hola, "
    case "French":
        prefix = "Bonjour, "
    default:
        prefix = "Hello, "
    }
    return
}

func Hello(name, language string) string {
    if name == "" {
        name = "World"
    }

    return greetingPrefix(language) + name
}
```

In this case we would add another subtest to the `TestHello` test.

```go
func TestHello(t *testing.T) {
    t.Run("saying hello to people", func(t *testing.T) {
        got := Hello("Chris", "")
        want := "Hello, Chris"
        assertCorrectMessage(t, got, want)
    })

    t.Run("empty string defaults to 'world'", func(t *testing.T) {
        got := Hello("", "")
        want := "Hello, World"
        assertCorrectMessage(t, got, want)
    })

    t.Run("in Spanish", func(t *testing.T) {
        got := Hello("Elodie", "Spanish")
        want := "Hola, Elodie"
        assertCorrectMessage(t, got, want)
    })

    t.Run("in French", func(t *testing.T) {
        got := Hello("Elodie", "French")
        want := "Bonjour, Elodie"
        assertCorrectMessage(t, got, want)
    })
}
```

Note: Make sure to continue to follow red-green-refactor when writing tests.

- See it fail
- Make the test pass
- Refactor
- Repeat

## Property Based Tests

```Go
func TestRomanNumerals(t *testing.T) {
	cases := []struct {
		Description string
		Arabic      int
		Want        string
	}{
		{"1 gets converted to I", 1, "I"},
		{"2 gets converted to II", 2, "II"},
	}

	for _, test := range cases {
		t.Run(test.Description, func(t *testing.T) {
			got := ConvertToRoman(test.Arabic)
			if got != test.Want {
				t.Errorf("got %q, want %q", got, test.Want)
			}
		})
	}
}
```

We can now easily add more cases without having to write any more test boilerplate.

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

