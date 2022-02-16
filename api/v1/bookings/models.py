from django.db import models
from api.v1.users.models import Patient, Doctor
import shortuuid
# Create your models here.

class AppointmentSlot(models.Model):

    OPEN = 'OP'
    CLOSED = 'CL'

    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (CLOSED, 'Closed')
    ]

    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=OPEN)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Appointment {self.start_time}'

class Booking(models.Model):
    #pending, approved, canceled, unpaid, completed, processing, rejected

    PENDING = 'PE'
    APPROVED = 'AP'
    REJECTED = 'RJ'
    CANCELED = 'CA'
    PROCESSING = 'PR'
    COMPLETED = 'CO'

    PAID = 'P'
    UNPAID = 'U'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (CANCELED, 'Canceled'),
        (COMPLETED, 'Completed')
    ]

    PAYMENT_CHOICES = [
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid')
    ]

    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    booking_slot = models.OneToOneField(AppointmentSlot, on_delete=models.SET_NULL, null=True)
    booking_reference = models.UUIDField(default=shortuuid.uuid, editable=False)
    booking_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    payment_status = models.CharField(max_length=2, choices=PAYMENT_CHOICES, default=UNPAID)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'Appointment - ' + str(self.booking_reference)