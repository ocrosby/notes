# Type Comparison

Example:

```python
name: str = 'Bob'
number: int = 123
x: str = 'x'

print(type(name) == type(x))  # True
```

Note: This is not a recommended way to compare types in Python. Instead, use `isinstance()` to check if an object is 
an instance of a class or subclass.

Another Example:

```python
name: str = 'Bob'
number: int = 123
x: str = 'x'

print(isinstance(name, str))  # True
print(isinstance(number, int))  # True
```

This is the recommended way to check the type of an object in Python.
