from django.contrib import admin
from .models import Patient, Doctor, User

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(User)