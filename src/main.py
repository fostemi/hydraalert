from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
recieving_number = os.environ['RECIEVING_PHONE_NUMBER']

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18334721063',
    body='Lets get hydrated',
    to=recieving_number
)

