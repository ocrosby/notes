# FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Installation

```Shell
pip install fastapi
```

## Usage

To create a FastAPI application, you need to create an instance of the `FastAPI` class.

```Python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

To run the application, you can use the `uvicorn` command:

```Shell
uvicorn main:app --reload
```

## References

- [FastAPI](https://fastapi.tiangolo.com)
