# Builder Pattern

The Builder pattern is a creational pattern that allows constructing complex objects step by step. The pattern allows to produce different types and representations of an object using the same construction code.

## Problem

Imagine a complex object that requires laborious, step-by-step initialization of many fields and nested objects. The object can be constructed in one shot, but the construction code would be hard to read and maintain.

## Solution

The Builder pattern suggests extracting the object construction code out of its own class and into a set of separate objects called builders. The same construction process can create different representations of the object.

## Structure

- `Director`: constructs objects using the builder interface.
- `Builder`: declares the steps to build the product.
- `ConcreteBuilder`: implements the builder interface to construct and assemble parts of the product.
- `Product`: represents the complex object under construction.
- `Client`: uses the director to construct the product.

## Example

Suppose we have a `Car` class with many fields that need to be initialized. We can use the Builder pattern to construct the `Car` object step by step.

```python
class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"
```

The `CarBuilder` class defines the steps to build a `Car` object.

```python
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_year(self, year):
        self.car.year = year
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car
```

The `CarDirector` class constructs the `Car` object using the `CarBuilder`.

```python
class CarDirector

    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        return self.builder.set_make("Toyota") \
            .set_model("Corolla") \
            .set_year(2020) \
            .set_color("Red") \
            .build()
```

The client code constructs a `Car` object using the `CarDirector`.

```python

builder = CarBuilder()
director = CarDirector(builder)
car = director.construct()
print(car)  # 2020 Toyota Corolla (Red)
```

## Applicability

Use the Builder pattern when:

- The object to be constructed has many fields that require complex initialization.
- The object construction code must be independent of the final representation.
- The same construction process can create different representations of the object.
- The construction process must allow constructing the object step by step.
- The construction process must be able to produce different types and representations of the object.
- The object creation code must be easy to read and maintain.
- The object creation code must be reusable.
- The object creation code must be testable.
- The object creation code must be flexible.
- The object creation code must be extensible.
- The object creation code must be decoupled from the client code.
- The object creation code must be able to construct complex objects.
