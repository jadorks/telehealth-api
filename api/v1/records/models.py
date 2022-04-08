from django.db import models
from api.v1.users.models import Patient, Doctor
from api.v1.bookings.models import Booking

# Create your models here.
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.patient}'s Medical Record"

class RecordItem(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Booking, null=True, on_delete=models.SET_NULL)
    diagnosis = models.TextField()
    recommendation = models.TextField()
    medication = models.TextField()
    face_analysis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medical_record} - Record {self.id}"
