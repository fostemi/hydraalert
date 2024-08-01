from read_google_spreadsheet import parse_spreadsheet_id

def test_parse_spreadsheet_id():
    expected_sheet_id = "1QPrWQh2f8m0EFWZF_Qf_AlE6ErnNjTGQYKNfwBxQqgE"
    got_sheet_id = parse_spreadsheet_id("https://docs.google.com/spreadsheets/d/1QPrWQh2f8m0EFWZF_Qf_AlE6ErnNjTGQYKNfwBxQqgE/")
    assert got_sheet_id == expected_sheet_id, "Should be " + expected_sheet_id + ". got " + got_sheet_id
