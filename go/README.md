# Go Notes

Using gcflags

- Sharing down typically stays on the stack
- Sharing up typically escapes to the heap

To print if variables escape to the heap

```Shell
go build -gcflags="-m -l"
```

## References

- [Stack or Heap](https://golang.org/doc/faq#stack_or_heap)
