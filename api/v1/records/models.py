from django.db import models
from api.v1.users.models import Patient, Doctor
from api.v1.bookings.models import Booking


class RecordItem(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Booking, null=True, on_delete=models.SET_NULL)
    diagnosis = models.TextField()
    recommendation = models.TextField()
    medication = models.TextField()
    face_analysis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - Record {self.id}"
