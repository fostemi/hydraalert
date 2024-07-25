from read_hydration_times import *

def test_non_converted_time():
    assert convert_to_millitary_time('1:00:00 AM') == '1:00:00', "Should be 1:00:00"

def test_converted_single_digit():
    assert convert_to_millitary_time('1:00:00 PM') == '13:00:00', "Should be 13:00:00"

def test_converted_double_digit():
    assert convert_to_millitary_time('11:00:00 PM') == '23:00:00', "Should be 23:00:00"

def test_parse_spreadsheet_id():
    expected_sheet_id = "1QPrWQh2f8m0EFWZF_Qf_AlE6ErnNjTGQYKNfwBxQqgE"
    got_sheet_id = parse_spreadsheet_id("https://docs.google.com/spreadsheets/d/1QPrWQh2f8m0EFWZF_Qf_AlE6ErnNjTGQYKNfwBxQqgE/")
    assert got_sheet_id == expected_sheet_id, "Should be " + expected_sheet_id + ". got " + got_sheet_id

if __name__ == '__main__':
    test_non_converted_time()
    test_converted_single_digit()
    test_converted_double_digit()
    test_parse_spreadsheet_id()
    print("Everything Passed")
