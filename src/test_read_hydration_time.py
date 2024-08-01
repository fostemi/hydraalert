from read_hydration_times import *

def test_non_converted_time():
    assert convert_to_millitary_time('1:00:00 AM') == '1:00:00', "Should be 1:00:00"

def test_converted_single_digit():
    assert convert_to_millitary_time('1:00:00 PM') == '13:00:00', "Should be 13:00:00"

def test_converted_double_digit():
    assert convert_to_millitary_time('11:00:00 PM') == '23:00:00', "Should be 23:00:00"
