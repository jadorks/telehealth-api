from django.contrib import admin
from .models import Booking, AppointmentSlot

# Register your models here.
admin.site.register(Booking)
admin.site.register(AppointmentSlot)