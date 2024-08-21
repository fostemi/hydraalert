import pytest
from read_workouts import build_workout_program
from user import User

@pytest.fixture()
def user():
    print("setup")
    user = User(1, build_workout_program(), '06:00:00', '2196698586')
    yield user
    print("teardown")

class TestUser:
    pass
