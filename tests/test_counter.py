from lib.counter import *


""" 
count starts at 0

"""

def test_counter_starts_at_0():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

"""
add a given number to the count
"""

def test_add_a_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

"""
add multiple numbers to the count
"""

def test_add_multiple_nums():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far."

