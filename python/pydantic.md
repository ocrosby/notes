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

You can also do this by unpacking a dictionary 

```python
person_data = {
    "name": "Alice",
    "age": 30,
    "city": "Raleigh
}

person = Person(**person_data)

# If you don't provide a value for a field, the default value will be used

print(person.name)
print(person.age)
print(person.city)
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


Validating an email string

```python
from pydantic import BaseModel, EmailStr

class Person(BaseModel):
    email: EmailStr
    
person = Person(email="something")

# This will raise a validation error because the email is not a valid email address
```

Custom Validation

```python
from pydantic import validator, BaseModel, ValidationError



class Person(BaseModel):
    name: str
    age: int
    city: str

    @validator("age")
    def validate_age(cls, v):
        if v < 0:
            raise ValueError("Age must be greater than 0")
        return v
        
    try:
        person = Person(name="Alice", age=-1, city="New York")
    except ValidationError as e:
        print(e)
```

JSON Serialization
    
```python
person_json_str = user.json()
```

If you want to convert a pydantic model to a dictionary, you can use the `dict()` function.

```python
person_dict = dict(person)
```

or 
    
```python
person_dict = person.dict()
```

If you want to convert a dictionary into a pydantic model

```python
json_str = '{"name": "Alice", "age": 30, "city": "New York"}'

person = Person.parse_raw(json_str)
```


git
## References

- [Pydantic](https://pydantic-docs.helpmanual.io/)
