import pytest
from lib.password_checker import *

"""
Happy path
Length of password is 8 characters or more
Return True
"""

def test_password_is_8_or_more_characters():
    pass_checker = PasswordChecker()
    assert pass_checker.check("Makers12") == True

"""
If length of password is less than 8
Rerturn the following error message:
"Invalid password, must be 8+ characters."
"""

def test_password_is_less_than_8_characters():
    pass_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        pass_checker.check("Makers")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."