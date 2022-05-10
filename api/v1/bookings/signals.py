from django.db.models.signals import post_save,post_delete
from api.v1.bookings.models import Booking
from telehealth.utlis import send_message

def update_booking_slot(sender, instance, **kwargs):
    booking_slot = instance.booking_slot
    booking_slot.status = 'CL'
    booking_slot.save()

    booking_datetime = booking_slot.start_time
    booking_date = booking_datetime.strftime("%a %d %b %Y")
    booking_time = booking_datetime.strftime("%I:%M %p")
    booking_doctor = instance.doctor
    booking_patient = instance.patient

    patient_msg = f"Your consultation for {booking_date} at {booking_time} with {booking_doctor.doctor.first_name} {booking_doctor.doctor.last_name} has been created." 
    doctor_msg = f"You have a new consultation for {booking_date} at {booking_time} with {booking_patient.patient.first_name} {booking_patient.patient.last_name}"
    send_message(patient_msg, "+233247754809")
    send_message(doctor_msg, "+233247754809")


post_save.connect(update_booking_slot, sender=Booking, dispatch_uid="created_booking")

def reset_booking_slot(sender, instance, **kwargs):
    booking_slot = instance.booking_slot
    booking_slot.status = 'OP'
    booking_slot.save()
    booking_datetime = booking_slot.start_time
    booking_date = booking_datetime.strftime("%a %d %b %Y")
    booking_time = booking_datetime.strftime("%I:%M %p")
    booking_doctor = instance.doctor
    booking_patient = instance.patient

    patient_msg = f"Your consultation for {booking_date} at {booking_time} with {booking_doctor.doctor.first_name} {booking_doctor.doctor.last_name} has been canceled."
    doctor_msg = f"Your consultation for {booking_date} at {booking_time} with {booking_patient.patient.first_name} {booking_patient.patient.last_name} has been canceled"
    send_message(patient_msg, "+233247754809")
    send_message(doctor_msg, "+233247754809")

post_delete.connect(reset_booking_slot, sender=Booking, dispatch_uid='deleted_booking')