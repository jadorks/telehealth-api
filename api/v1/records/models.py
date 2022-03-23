from django.db import models
from api.v1.users.models import Patient, Doctor

# Create your models here.
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.patient}'s Medical Record"
