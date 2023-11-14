from lib.gratitudes import *

"""
check for blank list
"""

def test_blank_list():
    grat = Gratitudes()
    assert grat.gratitudes == []

"""
test add a gratitude
"""

def test_add_grat():
    grat = Gratitudes()
    grat.add("tests")
    assert grat.format() == "Be grateful for: tests"

"""
test multiple gratitudes
"""

def test_multiple_grats():
    grat = Gratitudes()
    grat.add("tests")
    grat.add('pairs')
    assert grat.format() == "Be grateful for: tests, pairs"

"""
test more grats
"""

def test_three_grats():
    grat = Gratitudes()
    grat.add("tests")
    grat.add('pairs')
    grat.add("")
    assert grat.format() == "Be grateful for: tests, pairs, "