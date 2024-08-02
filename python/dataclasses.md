# Dataclasses

Dataclasses are a way to define classes that are mostly used to store data. They are similar to namedtuples, but with more flexibility.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

person = Person("Alice", 30, "New York")
print(person)
``` 

## Default Values

You can set default values for dataclass fields.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int = 0
    city: str = "New York"

person = Person("Alice")
print(person)
```

## Frozen Dataclasses

You can make dataclasses immutable by setting the `frozen` parameter to `True`.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    city: str

person = Person("Alice", 30, "New York")
print(person)

# This will raise an error
person.age = 31
```

## Inheritance

You can inherit from dataclasses.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

@dataclass
class Employee(Person):
    company: str

employee = Employee("Alice", 30, "New York", "Google")
print(employee)
```


## References

- [Dataclasses - Python Documentation](https://docs.python.org/3/library/dataclasses.html)
- [Dataclasses - Real Python](https://realpython.com/python-data-classes/)
- [Dataclasses - GeeksforGeeks](https://www.geeksforgeeks.org/data-classes-in-python/)
- [Dataclasses - PyMOTW](https://pymotw.com/3/dataclasses/index.html)
