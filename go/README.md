# Go Notes

Using gcflags

- Sharing down typically stays on the stack
- Sharing up typically escapes to the heap

To print if variables escape to the heap

```Shell
go build -gcflags="-m -l"
```

Compiler Flags

- go help build
- go tool compile -h
- go build -gcflags "-m=2"

## References

- [Stack or Heap](https://golang.org/doc/faq#stack_or_heap)
- [Go Blueprint](https://go-blueprint.dev/)
- [Go Blueprint GitHub](https://github.com/Melkeydev/go-blueprint)
- [Go By Example](https://gobyexample.com)
- [Effective Go](https://go.dev/doc/effective_go)
- [Lets Go Book](https://lets-go.alexedwards.net/)
- [Lets Go Further Book](https://lets-go-further.alexedwards.net/#packages)
- [Learn Go With Tests](https://quii.gitbook.io/learn-go-with-tests)

## YouTube Channels

- [Anthony GG](https://www.youtube.com/@anthonygg_)
- [Melkey](https://www.youtube.com/@MelkeyDev)
- [Tutorial Getting started with multi-module workspaces](https://go.dev/doc/tutorial/workspaces)