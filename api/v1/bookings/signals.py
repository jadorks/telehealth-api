from django.db.models.signals import post_save
from api.v1.bookings.models import Booking

def update_booking_slot(sender, instance, **kwargs):
    booking_slot = instance.booking_slot
    booking_slot.status = 'CL'
    booking_slot.save()
    # todo: notify both doctor and patient about booking
    # bad place to say, this but do a cron job that would create the rooms on the day of appointment and send link to both doctor and patient

post_save.connect(update_booking_slot, sender=Booking, dispatch_uid="created_booking")