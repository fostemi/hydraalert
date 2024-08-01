"""Twilio messaging env setting and sending messages given the times."""
import os
import os.path
import time
from datetime import datetime
from twilio.rest import Client
from read_hydration_times import parse_hydration_times

ACCOUNT_SID = os.environ['TWILIO_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
RECIEVING_NUMBER = os.environ['RECIEVING_PHONE_NUMBER']
SEND_NUMBER = os.environ['SEND_PHONE_NUMBER']

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

def schedule_texts():
    """Forever loop triggers messages when time equals message time."""
    message_times = parse_hydration_times()
    day = get_current_day()
    while True:
        if get_current_time() in message_times:
            send_message('Lets get hydrated', RECIEVING_NUMBER)
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
