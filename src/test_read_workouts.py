import pytest
from read_workouts import build_workout_program, Workout

@pytest.fixture()
def workout_program():
    print("setup")
    workout_program = build_workout_program()
    yield workout_program
    print("teardown")

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

    def test_parse_swim_row(self, workout_program):
        want = [Workout(2, 8, 'Swim', '1 mile'), Workout(4, 8, 'Swim', '1 mile')]
        got = workout_program.workouts
        assert_workouts_eq(got[0], want[0])
        assert_workouts_eq(got[1], want[1])

    def test_parse_bike_row(self, workout_program):
        want = [Workout(5, 8, 'Bike', '16 miles'), Workout(6, 8, 'Bike', '24 miles')]
        got = workout_program.workouts
        assert_workouts_eq(got[2], want[0])
        assert_workouts_eq(got[3], want[1])
        
    def test_parse_run_row(self, workout_program):
        want = [Workout(3, 8, 'Run', '7 miles'), Workout(6, 8, 'Run', '5 miles')]
        got = workout_program.workouts
        assert_workouts_eq(got[4], want[0])
        assert_workouts_eq(got[5], want[1])
    
    def test_get_workout_by_day(self, workout_program):
        want = Workout(3, 8, 'Run', '7 miles')
        got = workout_program.get_workout_by_day(8, 3)
        assert_workouts_eq(got, want)

