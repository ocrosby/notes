# Pytest

Pytest is a testing framework that makes it easy to write simple tests. It is a popular choice for testing in 
Python because it is easy to use and has a simple syntax. Pytest is built on top of the `unittest` module and is 
compatible with `unittest` fixtures.

## Installation

```Shell
pip install pytest pytest-cov pytest-mock
```

## Usage

To run a test, you can use the `pytest` command:

```Shell
pytest test_sample.py
```

This command will run the test in the `test_sample.py` file.

## Writing Tests

- Tests should be in a file with a name like `test_xxx.py`
- The test function must start with the word `test`
- The test function takes one argument only `test`
- To use the `assert` statement you do not need to import any module
- The `assert` statement is used to check if a condition is `True`
- If the condition is `False`, the `assert` statement will raise an `AssertionError`
- The `assert` statement can take an optional message argument



```Python

```

## Running Tests

- Run your tests with `pytest`
- You can run all tests in a directory with `pytest <directory>`
- You can run a specific test with `pytest <test_file.py>::<test_function>`
- Use the `-v` flag to see the output of the tests
- Use the `-k` flag to run tests that match a specific keyword

```Shell
pytest -v
```

```Shell
pytest -k test_something
```

## Fixtures

Fixtures are functions that run before and after tests. They are used to set up the test environment and clean up

```Python
import pytest

@pytest.fixture
def setup():
    print("\nSetup")

def test_something(setup):
    print("Test something")
    assert True

def test_something_else(setup):
    print("Test something else")
    assert True
```

## Parametrized Tests

Parametrized tests allow you to run the same test with different inputs. You can use the `@pytest.mark.parametrize` 
decorator to specify the inputs and expected outputs for the test.

```Python
import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (3, 5, 8),
    (2, 2, 4),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

So when the test_add function is run, it will run three times with the inputs (1, 2), (3, 5), and (2, 2).
The third number in the tuple is the expected output. We use that in the assertion to check if the function is 
working correctly.


## Mocking

Mocking is a technique used to replace a function or object with a fake version. This is useful when you want to
test a function that depends on another function that is not yet implemented.

```Python
from unittest.mock import patch

def get_data():
    return "Real data"

def use_data():
    data = get_data()
    return data

def test_use_data():
    with patch("__main__.get_data") as mock_get_data:
        mock_get_data.return_value = "Mock data"
        assert use_data() == "Mock data"
```

In this example, we are testing the `use_data` function. The `use_data` function calls the `get_data` function.
We use the `@patch` decorator to replace the `get_data` function with a mock version that returns "Mock data".
This allows us to test the `use_data` function without having to implement the `get_data` function.

## References

- [Pytest](https://docs.pytest.org)
- [Pytest Documentation](https://docs.pytest.org/en/stable/contents.html)
- [Pytest Quick Start Guide](https://docs.pytest.org/en/stable/getting-started.html)
- [Pytest Fixtures](https://docs.pytest.org/en/stable/fixture.html)
- [Pytest Parametrize](https://docs.pytest.org/en/stable/parametrize.html)
- [Pytest Mocking](https://docs.pytest.org/en/stable/monkeypatch.html)
- [Pytest Plugins](https://docs.pytest.org/en/stable/plugins.html)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Python Testing with Pytest](https://www.pluralsight.com/courses/python-testing-pytest)
