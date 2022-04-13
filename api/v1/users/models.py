from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'

    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    phone_number = models.CharField(max_length=20, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, blank=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

class Doctor(models.Model):
    ONLINE = 'ON'
    OFFLINE = 'OF'
    BUSY = 'BU'

    STATUS_CHOICES = [
        (OFFLINE, 'Offline'),
        (ONLINE, 'Online'),
        (BUSY, 'Busy')
    ]

    doctor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, blank=False, default=ONLINE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.doctor.username

class Patient(models.Model):
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dob = models.DateField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.username