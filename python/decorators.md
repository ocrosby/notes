# Decorators

Decorators are a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

There are generally three types of decorators in Python:

1. Function decorators
2. Class decorators
3. Method decorators

## Function Decorators

Function decorators are used to modify the behavior of a function or a method. They are defined with the `@decorator` syntax, where `decorator` is the name of the decorator function.

Here is an example of a simple function decorator:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

In this example, the `my_decorator` function is defined, which takes a function as an argument and returns a new function that wraps the original function. The `@my_decorator` syntax is used to decorate the `say_hello` function with the `my_decorator` function.

## Class Decorators

Class decorators are used to modify the behavior of a class. They are defined with the `@decorator` syntax, where `decorator` is the name of the decorator class.

Here is an example of a simple class decorator:

```python
class MyClassDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self):
        print("Something is happening before the class is called.")
        obj = self.cls()
        print("Something is happening after the class is called.")
        return obj

@MyClassDecorator
class MyClass:
    def __init__(self):
        print("MyClass is called.")

obj = MyClass()
```

In this example, the `MyClassDecorator` class is defined, which takes a class as an argument and returns a new class that wraps the original class. The `@MyClassDecorator` syntax is used to decorate the `MyClass` class with the `MyClassDecorator` class.

## Method Decorators

Method decorators are used to modify the behavior of a method in a class. They are defined with the `@decorator` syntax, where `decorator` is the name of the decorator function.

Here is an example of a simple method decorator:

```python
def my_method_decorator(func):
    def wrapper(self):
        print("Something is happening before the method is called.")
        func(self)
        print("Something is happening after the method is called.")
    return wrapper
    
class MyClass:
    @my_method_decorator
    def my_method(self):
        print("My method is called.")
        
obj = MyClass()
obj.my_method()
```

In this example, the `my_method_decorator` function is defined, which takes a method as an argument and returns a new method that wraps the original method. The `@my_method_decorator` syntax is used to decorate the `my_method` method in the `MyClass` class.

## Decorator with Arguments

Decorators can also take arguments to customize their behavior. To create a decorator with arguments, you need to define a decorator function that takes the arguments and returns a decorator function that takes the function to be decorated.

Here is an example of a decorator with arguments:

```python
def my_decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper():
            print(f"Something is happening before the function is called with arguments {arg1} and {arg2}.")
            func()
            print("Something is happening after the function is called.")
        return wrapper
    return decorator
    
@my_decorator_with_args("arg1", "arg2")
def say_hello():
    print("Hello!")
    
say_hello()

```

In this example, the `my_decorator_with_args` function is defined, which takes two arguments and returns a decorator function that takes a function as an argument. The `@my_decorator_with_args("arg1", "arg2")` syntax is used to decorate the `say_hello` function with the `my_decorator_with_args` function.

## Chaining Decorators

Decorators can be chained together to apply multiple decorators to a function or a method. To chain decorators, you need to apply them in the order you want

Here is an example of chaining decorators:

```python
def my_decorator1(func):
    def wrapper():
        print("Decorator 1: Something is happening before the function is called.")
        func()
        print("Decorator 1: Something is happening after the function is called.")
    return wrapper
    
def my_decorator2(func):
    def wrapper():
        print("Decorator 2: Something is happening before the function is called.")
        func()
        print("Decorator 2: Something is happening after the function is called.")
    return wrapper
    
@my_decorator1
@my_decorator2
def say_hello():
    print("Hello!")
    
say_hello()

```

## Built-in Decorators

Python provides several built-in decorators that can be used to modify the behavior of functions and methods. Some of the commonly used built-in decorators are:

- `@staticmethod`: Decorates a method that does not access or modify the class instance.
- `@classmethod`: Decorates a method that takes the class itself as the first argument.
- `@property`: Decorates a method that can be accessed as an attribute.
- `@abstractmethod`: Decorates a method that must be implemented by a subclass.
- `@functools.wraps`: Decorates a function to preserve its metadata.
- `@functools.lru_cache`: Decorates a function to cache its return values.
- `@functools.singledispatch`: Decorates a function to provide single-dispatch generic functions.
- `@functools.total_ordering`: Decorates a class to provide rich comparisons.
- `@contextlib.contextmanager`: Decorates a generator function to create a context manager.
- `@asyncio.coroutine`: Decorates a generator function to create a coroutine.


## Conclusion

Decorators are a powerful feature in Python that allows you to add new functionality to existing objects without modifying their structure. They are commonly used to modify the behavior of functions and classes, and Python provides several built-in decorators that can be used to achieve this. By understanding how decorators work, you can write more flexible and reusable code in Python.

## References

- [Python Decorators - The Complete Guide from ArjanCodes](https://arjan.codes/python-decorators/)
- [Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [Decorators in Python](https://www.youtube.com/watch?v=WpF6azYAxYg)
- [Python Decorators - Video](https://www.youtube.com/watch?v=9oyr0mocZTg)
- [Decorators In Python](https://www.geeksforgeeks.org/decorators-in-python/)
- [Automate with Python - Video](https://www.youtube.com/watch?v=PXMJ6FS7llk)
- [Python Decorators - Video](https://www.youtube.com/watch?v=9oyr0mocZTg)

