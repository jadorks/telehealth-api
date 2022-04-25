from rest_framework import serializers
from api.v1.bookings.serializers import BookingSerializer

from api.v1.users.serializers import DoctorSerializer, PatientSerializer
from . import models


class RecordItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RecordItem
        fields = '__all__'

class RecordItemListSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=False, read_only=True)
    doctor = DoctorSerializer(many=False, read_only=True)
    booking_id = BookingSerializer(many=False, read_only=True)

    class Meta:
        model = models.RecordItem
        fields = '__all__'