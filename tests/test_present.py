import pytest
from lib.present import *

"""
Test for wrapping and unwrapping
Happy path / case 123
"""

def test_wrap_then_unwrap():
    present = Present()
    present.wrap("toys")
    assert present.unwrap() == "toys"

"""
When there is already a present
The user should see following message:
"A contents has already been wrapped."
"""

def test_present_already_wrapped():
    present = Present()
    present.wrap("toys")
    with pytest.raises(Exception) as e:
        present.wrap("toy_car")
    error_message = str(e.value) # <-- New code
    assert error_message == "A contents has already been wrapped."

"""
If there is not a present 
and you try to unwrap it
The user should see following message:
"No contents have been wrapped."
"""

def test_no_present_to_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value) # <-- New code
    assert error_message == "No contents have been wrapped."

"""
If a present has already been wrapped
And you try to wrap another present
When you unwrap it should return the original present
"""

def test_double_wrap_then_unwrap():
    present = Present()
    present.wrap("toys")
    with pytest.raises(Exception) as e:
        present.wrap("toy_car")
    assert present.unwrap() == "toys"

