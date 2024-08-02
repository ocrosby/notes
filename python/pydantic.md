# Pydantic

Pydantic is a data validation and settings management using Python type annotations.

## Installation

```Shell
pip install pydantic
```

## Usage

To create a Pydantic model, you need to inherit from the `BaseModel` class.

```Python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str

person = Person(name="Alice", age=30, city="New York")
print(person)
```

## Default Values

You can set default values for Pydantic models.

```Python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int = 0
    city: str = "New York"

person = Person(name="Alice")
print(person)
```

## Data Validation

Pydantic models will raise a `ValidationError` if the data does not match the type annotation.

```Python
from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    name: str
    age: int
    city: str

try:
    person = Person(name="Alice", age="30", city="New York")
except ValidationError as e:
    print(e)
```

This will raise a `ValidationError` because the `age` field is a string, not an integer.

## References

- [Pydantic](https://pydantic-docs.helpmanual.io/)
