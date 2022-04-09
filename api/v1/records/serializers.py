from rest_framework import serializers
from . import models
from api.v1.users.models import Patient, Doctor
from api.v1.bookings.models import Booking

class RecordSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(many=False, queryset=Patient.objects.all())

    class Meta:
        model = models.MedicalRecord
        fields = '__all__'

class RecordItemSerializer(serializers.ModelSerializer):
    medical_record = serializers.PrimaryKeyRelatedField(many=False, queryset=models.MedicalRecord.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(many=False, queryset=Doctor.objects.all())    
    booking_id = serializers.PrimaryKeyRelatedField(many=False, allow_null=True, queryset=Booking.objects.all())

    class Meta:
        model = models.RecordItem
        fields = '__all__'