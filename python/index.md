# Python

## Setup

Because of issues with requests and urllib3, I am trying to install
Python 3.12 from homebrew as follows:

```bash
brew install python@3.12
```

To ensure you are using the proper version of Python, edit your ~/.zshrc file
to include the following:

```bash
export PATH="/usr/local/opt/python@3.12/bin:$PATH"
```

Then make sure to reload your shell configuration

```bash
source ~/.zshrc
```

Verify the version of Python you are using

```bash
python3 --version
```

Also in PyCharm I had to create a new local interpreter and point it to

```/opt/homebrew/Cellar/python@3.12/3.12.4/bin/python3.12```

To set the default Python interpreter in PyCharm to the one located at /opt/homebrew/Cellar/python@3.12/3.12.4/bin/python3.12, follow these steps:

1. Open PyCharm.
2. Go to PyCharm > Preferences (or File > Settings on Windows/Linux).
3. Navigate to Project: <Your Project Name> > Python Interpreter.
4. Click on the gear icon next to the current interpreter and select Add....
5. Choose System Interpreter.
6. Browse to /opt/homebrew/Cellar/python@3.12/3.12.4/bin/python3.12 and select it.
7. Click OK to apply the changes.

To set this interpreter as the default for all new projects:


Creating a new virtual environment

```bash
$ python3 -m venv .venv
```

Creating an editable install

```bash
$ python -m pip install -e path/to/SomeProject
```

## Iterate With enumerate() instead of range(len())

Instead of this

```python
data = [1, 2, -4, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

print(data)
```

Use this

```python
data = [1, 2, -4, -3]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

print(data)
```

## Use List Comprehensions Instead of for raw loops

Instead of this

```python
squares = []
for i in range(10):
    squares.append(i*i)

print(squares)
```

Use this

```python
squares = [i*i for i in range(10)]
print(squares)
```

## Sort complex iterables with sorted()

data = [3,5,1,10,9]
sorted_data = sorted(data, reverse=True)

print(sorted_data)

data = [{"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9}]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)


## Store unique values with Sets

```python
my_list = [1,2,3,4,5,6,7,7,7,7]
my_set = set(my_list)
print(my_set)

# You can create a set directly with curly braces
primes = {2,3,5,7,11,13,17,19}
print(primes)

# There are methods for calculating the intersections and differences between sets.
```

## Save Memory with Generators

```python
my_list = [i for i in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")
```

## Define default values in Dictionaries with .get() and .setdefault()

```python
my_dict = {"item": "football", "price": 10.00}
count = my_dict["count"] # raises a key error

# instead use

count = my_dict.get("count") # returns None

count = my_dict.get("count") # returns None

count = my_dict.get("count", 0) # returns 0 but doesn't alter the dict

count = my_dict.setdefault("count", 0) # returns 0 and alters the dict
print(count)
print(my_dict)
```

## Count hasable objects with collections.Counter

```python
from collections import Counter

my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)

print(counter)

counter[11]
counter[10]

most_common = counter.most_common(1)
print(most_common)
print(most_common[0])
```

## Format strings with f-strings

## Concatinate strings with .join

```python
list_of_strings = ["Hello", "my", "friend"]

my_string = " ".join(list_of_strings)

print(my_string)
```

## Merge two dictionaries

```python
d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "New York"}

merged_dict = {**d1, **d2}

# The final dictionary has all three
```

## Simplify if statements for multiple checks

```python
colors = ["red", "green", "blue"]

c = "red"
if c in colors:
    print("is main color")
```

## References

- [Editable Installs](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs)
- [Pydantic](./pydantic.md)
- [Dataclasses](./dataclasses.md)
- [FastAPI](./fastapi.md)
- [Data Access Layer](./dal.md)
- [Write Robust API's In Python With Three Layer Architecture, FastAPI and Pydantic Models](https://medium.com/@yashika51/write-robust-apis-in-python-with-three-layer-architecture-fastapi-and-pydantic-models-3ef20940869c)
- [Python 3.12](https://www.python.org/downloads/release/python-312/)
