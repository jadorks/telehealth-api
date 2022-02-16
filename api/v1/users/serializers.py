from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User, Doctor, Patient

class DoctorSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True,)
    class Meta:
        model=Doctor
        fields = '__all__'

