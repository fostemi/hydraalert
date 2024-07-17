from twilio.rest import Client
from datetime import datetime
import os
import os.path

def set_environment():
    global account_sid, auth_token, recieving_number, twilio_client
    account_sid = os.environ['TWILIO_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    recieving_number = os.environ['RECIEVING_PHONE_NUMBER']
    twilio_client = Client(account_sid, auth_token)

def get_current_time():
    return str(datetime.now().time())[:-7]

def get_current_day():
    return datetime.now().date().day

def schedule_texts():
    message_times = get_hydration_times()
    day = get_current_day()
    while(True):
        if get_current_time() in message_times:
            send_message('Lets get hydrated', recieving_number)
            time.sleep(1)
        if get_current_day() != day:
            message_times = get_hydration_times()
            day = get_current_day()

def send_message(message, reciever):
    message = twilio_client.messages.create(
        from_='+18334721063',
        body=message,
        to=reciever
    )

def main():
    set_environment()
    schedule_texts()

if __name__ == "__main__":
    main()
