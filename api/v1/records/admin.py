from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MedicalRecord)
admin.site.register(models.RecordItem)