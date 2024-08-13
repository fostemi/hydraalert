from read_workouts import build_workout_program

def test_parse_workout_sheet_title():
    want = "Iron Man 13 Week Training Plan"
    workout_program = build_workout_program()
    got = workout_program.title
    assert got == want, "got " + got + " should be " + want

