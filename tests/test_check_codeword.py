from lib.check_codeword import *

def test_check_codeword_correct():
    codeword = "horse"
    assert check_codeword(codeword) == "Correct! Come in."

def test_check_codeword_almost():
    codeword = "h***e"
    assert check_codeword(codeword) == "Close, but nope."

def test_check_codeword_wrong():
    codeword = "test"
    assert check_codeword(codeword) == "WRONG!"