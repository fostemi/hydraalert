import pytest
from read_workouts import build_workout_program

@pytest.fixture()
def workout_program():
    print("setup")
    workout_program = build_workout_program()
    yield workout_program
    print("teardown")

class TestWorkoutProgram:
    def test_parse_workout_sheet_title(self, workout_program):
        want = "Iron Man 13 Week Training Plan"
        # workout_program = build_workout_program()
        got = workout_program.title
        assert got == want, "got " + got + " should be " + want


