import os
import os.path
import time
from build_message import build_morning_message, send_message
from utils import get_current_weekday

RECIEVING_NUMBER = os.environ['RECIEVING_PHONE_NUMBER']
# TODO: User input
PROGRAM_START_WEEK = 9

def handle_workout_messaging(workout_program):
    week = PROGRAM_START_WEEK
    current_day = get_current_weekday()
    workout = workout_program.get_workout_by_day(week, current_day)
    send_message(build_morning_message(workout), RECIEVING_NUMBER)
    if current_day == 6:
        week += 1
    time.sleep(1)

def handle_hydration_messaging():
    send_message('Lets get hydrated', RECIEVING_NUMBER)
    time.sleep(1)
