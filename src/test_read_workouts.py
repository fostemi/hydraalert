import pytest
from read_workouts import build_workout_program, parse_swim_row, Workout

@pytest.fixture()
def workout_program():
    print("setup")
    workout_program = build_workout_program()
    yield workout_program
    print("teardown")
@pytest.fixture()
def swim_week():
    print("setup swim tests")
    swim_week = ['8', 'Swim', 'Rest', '1 mile', '', '1 mile', '', '', 'Rest']
    yield swim_week
    print("teardown swim tests")

def assert_workouts_eq(got, want):
        assert got.day == want.day, "got " + str(got.day) + " should be " + str(want.day)
        assert got.week == want.week, "got " + str(got.week) + " should be " + str(want.week)
        assert got.excercise == want.excercise, "got " + got.excercise + " should be " + want.excercise
        assert got.distance == want.distance, "got " + got.distance + " should be " + want.distance

class TestWorkoutProgram:
    def test_parse_workout_sheet_title(self, workout_program):
        want = "Iron Man 13 Week Training Plan"
        got = workout_program.title
        assert got == want, "got " + got + " should be " + want

    def test_parse_swim_row(self, swim_week):
        want = Workout(2, 8, 'Swim', '1 mile')
        got = parse_swim_row(swim_week, 8)[0]
        assert_workouts_eq(got, want)
