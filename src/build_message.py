from utils import *
from twilio.rest import Client
import os
import os.path

ACCOUNT_SID = os.environ['TWILIO_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
SEND_NUMBER = os.environ['SEND_PHONE_NUMBER']

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

def build_morning_message(workout):
    file = open("goggins_transcript.txt", "r")
    goggins_transcript = file.read()
    file.close()
    prompt = f"""
    Read the following transcript delimited by triple backticks \
    and create a personality to give a motivational speech (75 \
    words max) for a workout in the excercise \
    {workout.excercise} for the distance {workout.distance}, here \
    is the transcript to build the motivational speech: 
    ```{goggins_transcript}```
    """
    response = get_completion(prompt)
    print(response)
    return response
    # return get_completion(prompt)

def send_message(message, reciever):
    """Helper function to send message."""
    message = twilio_client.messages.create(
        from_=SEND_NUMBER,
        body=message,
        to=reciever
    )
