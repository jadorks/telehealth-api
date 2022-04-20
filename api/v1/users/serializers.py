from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User, Doctor, Patient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class DoctorSerializer(serializers.ModelSerializer):
    doctor = UserSerializer(read_only=True, many=False)
    class Meta:
        model=Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    patient = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorRegistrationSerializer(RegisterSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True,)
    first_name = serializers.CharField(required=True,)
    last_name = serializers.CharField(required=True,)
    bio = serializers.CharField(required=True,)
    phone_number = serializers.CharField(required=True,)

    def get_cleaned_data(self):
        data = super(DoctorRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'bio': self.validated_data.get('bio', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(DoctorRegistrationSerializer, self).save(request)
        user.is_doctor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        doctor = Doctor(
            doctor = user,
            bio = self.cleaned_data.get('bio')
        )
        doctor.save()
        return user

class PatientRegistrationSerializer(RegisterSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True,)
    first_name = serializers.CharField(required=True,)
    last_name = serializers.CharField(required=True,)
    phone_number = serializers.CharField(required=True,)


    def get_cleaned_data(self):
        data = super(PatientRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'phone_number': self.validated_data.get('phone_number', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(PatientRegistrationSerializer, self).save(request)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        patient = Patient(
            patient = user,
        )
        patient.save()
        return user


