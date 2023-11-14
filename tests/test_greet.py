from lib.greet import *

def test_greet():
    name = "Zak"
    assert greet(name) == f"Hello, {name}!"