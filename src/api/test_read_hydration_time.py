from read_hydration_times import *

def test_non_converted_time():
    assert convert_to_millitary_time('1:00:00 AM') == '1:00:00', "Should be 1:00:00"

def test_converted_single_digit():
    assert convert_to_millitary_time('1:00:00 PM') == '13:00:00', "Should be 13:00:00"

def test_converted_double_digit():
    assert convert_to_millitary_time('11:00:00 PM') == '23:00:00', "Should be 23:00:00"

def test_parse_hydration_times():
    want = ['6:00:00', '8:30:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00', '17:00:00', '18:30:00', '20:00:00']
    got = parse_hydration_times()
    for i in range(len(want)):
        assert want[i] == got[i], "Got " + got[i] + " wanted " + want[i]
