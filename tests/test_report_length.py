from lib.report_length import *

def test_report_length():
    teststring = 'Zak'
    assert report_length(teststring) == f"This string was {len(teststring)} characters long."