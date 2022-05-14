import os
from twilio.rest import Client
from telehealth import settings

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
phone = settings.TWILIO_SMS_PHONE

client = Client(account_sid, auth_token)

def send_message(msg, recipient):
    print("trying to send msg jeff")
    client.messages.create(body=msg, from_=phone, to=recipient)


