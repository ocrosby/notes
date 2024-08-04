# Running Pytest in Parallel

Pytest can run tests in parallel to speed up the test suite. This is especially useful when you have a large test suite that takes a long time to run. Pytest can run tests in parallel by using the `-n` option to specify the number of workers to use.


## Installation

```Shell
pip install pytest
pip install pytest-xdist
```

The ```pytest-xdist``` plugin is required to run tests in parallel.


## Usage

To run tests in parallel, you can use the `-n` option to specify the number of workers to use. For example, to run tests using 4 workers, you can use the following command:

```Shell
pytest -n 4
```

This will run tests in parallel using 4 workers. You can adjust the number of workers based on the number of CPU cores available on your machine.

## References

- [Pytest Documentation](https://docs.pytest.org)
