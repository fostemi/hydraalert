from read_workouts import parse_workout_sheet_title

def test_parse_workout_sheet_title():
    want = "Iron Man 13 Week Training Plan"
    got = parse_workout_sheet_title()
    assert got == want, "got " + got + " should be " + want

