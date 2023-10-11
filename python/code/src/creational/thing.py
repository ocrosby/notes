from abc import ABCMeta, abstractmethod

from typing import List

class Thing:
    name: str

    def __init__(self, name: str = None):
        self.name = name

    def __repr__(self):
        return f"Thing({self.name})"

    def __str__(self) -> str:
        return self.name


class Builder(object):
    _instance: Thing

    def __init__(self):
        self._instance = None

    def build(self):
        self._instance = Thing()

    def build_name(self, name: str):
        self._instance.name = name

    def get_instance(self):
        return self._instance

class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self, name: str) -> Thing:
        pass


class Factory(AbstractFactory):
    builder: Builder

    def __init__(self, builder: Builder):
        self.builder = builder

    def create(self, name: str):
        self.builder.build()
        self.builder.build_name(name)

        return self.builder.get_instance()


class Loader(object):
    @staticmethod
    def load(names: List[str], factory: AbstractFactory) -> List[Thing]:
        return [factory.create(name) for name in names]

    @staticmethod
    def load_callable(names: List[str], factory: callable) -> List[Thing]:
        return [factory(name) for name in names]


def create_thing(name: str) -> Thing:
    builder = Builder()

    builder.build()
    builder.build_name(name)

    return builder.get_instance()

if __name__ == "__main__":
    names = ["thing1", "thing2", "thing3"]

    builder = Builder()
    factory = Factory(builder)
    things = Loader.load(names, factory)

    print(repr(things))

    things = Loader.load_callable(names, factory=create_thing)

    print(repr(things))

