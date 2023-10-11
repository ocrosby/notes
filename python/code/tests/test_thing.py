from src.thing import Thing

def test_repr():
    thing = Thing("thing")
    assert repr(thing) == "Thing(thing)"

def test_str():
    thing = Thing("something")
    assert str(thing) == "something"

