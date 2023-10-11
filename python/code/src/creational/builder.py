from thing import Thing

_instance: Thing

def thing() -> Thing:
    _instance = Thing()

    return _instance

def name(name: str) -> None:
    _instance.name = name

def get_instance() -> Thing:
    return _instance

