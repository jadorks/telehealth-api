import os
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

import twilio.jwt.access_token
import twilio.jwt.access_token.grants
import twilio.rest

from dotenv import load_dotenv


from api.v1.bookings.models import Booking
import uuid

load_dotenv()

# Create your views here.
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
api_key = os.environ["TWILIO_API_KEY_SID"]
api_secret = os.environ["TWILIO_API_KEY_SECRET"]
twilio_client = twilio.rest.Client(api_key, api_secret, account_sid)

# create a room when it's time for the appointment
# to create a room you need a room name
# the room name is generated from the algorithm
# once the room name is generated, the twilio create room function is called and the name is passed
# the name is stored in the appointment object with the room_id
# return the room_name and room_id as a json

# connecting to a room
# not really generate a link 
# so what happens is the booking uuid is passed to the join route
# when the route is hit, the function gets the booking
# and the booking is added to the session information
# the name of the room and then calls the token stuff for twilio which would use the room name to get the token
# token uses patient id and doctor id
# the medication route is not protected, has a form, and the form 

# selects appointment object with the matching room id and stuff
# get the patient from there and then use that info for the medical record form
# once the consultation is done, save the form and call end room.

def create_room(room_name):
    try:
        twilio_room = twilio_client.video.rooms.create(unique_name=room_name)
        return twilio_room
    except:
        print("failed to create room for booking")


def find_or_create_room(room_name, booking_id):
    try:
        twilio_room = twilio_client.video.rooms(room_name).fetch()
    except twilio.base.exceptions.TwilioRestException:
        twilio_room = twilio_client.video.rooms.create(unique_name=room_name, type="go")
        booking = get_object_or_404(Booking, booking_reference = booking_id)
        booking.save()

    room_sid = str(twilio_room.sid)


    room_data = {
        "room_name": room_name,
        "room_sid": room_sid
    }

    return room_data


def get_access_token(room_name):
    access_token = twilio.jwt.access_token.AccessToken(account_sid, api_key, api_secret, identity=uuid.uuid4().int)
    video_grant = twilio.jwt.access_token.grants.VideoGrant(room=room_name)
    access_token.add_grant(video_grant)
    return access_token

def end_room(request, room_sid):
    room = twilio_client.video.rooms(room_sid).fetch()
    return render(request, 'video_chat/complete.html')

