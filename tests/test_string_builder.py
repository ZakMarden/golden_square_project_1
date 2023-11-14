from lib.string_builder import *

"""
return blank string
"""

def test_blank_string():
    stringbuilder = StringBuilder()
    assert stringbuilder.output() == ""

"""
return added string
"""

def test_return_string():
    stringbuilder = StringBuilder()
    stringbuilder.add('word')
    assert stringbuilder.output() == 'word'

"""
return size of string
"""

def test_return_str_size():
    stringbuilder = StringBuilder()
    stringbuilder.add('word')
    assert stringbuilder.size() == 4

"""
test pass multiple string
"""

def test_return_multiple_string():
    stringbuilder = StringBuilder()
    stringbuilder.add('word')
    stringbuilder.add(' ')
    stringbuilder.add('word2')
    assert stringbuilder.output() == "word word2"

"""
return len of multiple strings
"""

def test_return_len_multiple_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add('word')
    stringbuilder.add(' ')
    stringbuilder.add('word2')
    assert stringbuilder.size() == 10

