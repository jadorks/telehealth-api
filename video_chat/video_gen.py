import datetime
from api.v1.bookings.models import Booking
from . utils import create_room
import namegenerator

def create_meeting_rooms():
    current_time = datetime.datetime.now().replace(second=0, microsecond=0)
    print(current_time)
    bookings = Booking.objects.filter(booking_slot__start_time = current_time).exclude(booking_status='CO')
    for booking in bookings:
        try:
            room_name = namegenerator.gen()
            twilio_room = create_room(room_name)
            booking.room_name = room_name
            booking.room_sid = str(twilio_room.sid)
            booking.save()
        except:
            print("failed to create room for:", booking.id)