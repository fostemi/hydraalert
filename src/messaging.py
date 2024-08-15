"""Twilio messaging env setting and sending messages given the times."""
import os
import os.path
import time
from datetime import datetime
from twilio.rest import Client
from read_hydration_times import parse_hydration_times
from read_workouts import build_workout_program

ACCOUNT_SID = os.environ['TWILIO_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
RECIEVING_NUMBER = os.environ['RECIEVING_PHONE_NUMBER']
SEND_NUMBER = os.environ['SEND_PHONE_NUMBER']
# TODO: User input
WAKE_UP = '19:59:00'

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

def schedule_texts():
    """Forever loop triggers messages when time equals message time."""
    message_times = parse_hydration_times()
    workout_program = build_workout_program()
    week = 8
    day = get_current_day()
    while True:
        if get_current_time() in message_times:
            send_message('Lets get hydrated', RECIEVING_NUMBER)
            time.sleep(1)
        if get_current_time() == WAKE_UP:
            current_day = get_current_weekday()
            workout = workout_program.get_workout_by_day(week, current_day)
            send_message('Workout time' + workout.excercise + " for " + workout.distance, RECIEVING_NUMBER)
            if current_day == 6:
                week += 1
            time.sleep(1)
        if get_current_day() != day:
            message_times = parse_hydration_times()
            day = get_current_day()

def send_message(message, reciever):
    """Helper function to send message."""
    message = twilio_client.messages.create(
        from_=SEND_NUMBER,
        body=message,
        to=reciever
    )

def get_current_time():
    """Helper function to get current time."""
    return str(datetime.now().time())[:-7]

def get_current_day():
    """Helper function to get current day."""
    return datetime.now().date().day

def get_current_weekday():
    return int(datetime.today().strftime('%w'))
