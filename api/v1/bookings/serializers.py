from rest_framework import serializers
from . import models

from api.v1.users.models import Patient, Doctor

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppointmentSlot
        fields = '__all__'


class BookingListSerializer(serializers.ModelSerializer):
    booking_slot = SlotSerializer(many=False, read_only=True)
    
    class Meta:
        model = models.Booking
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'