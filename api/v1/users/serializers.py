from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User, Doctor, Patient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'phone_number']

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
    bio = serializers.CharField(required=True,)
    gender = serializers.ChoiceField(choices=User.GENDER)
    phone_number = serializers.CharField(required=True,)

    def get_cleaned_data(self):
        data = super(DoctorRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'bio': self.validated_data('bio', ''),
            'phone_number': self.validated_data('phone_number', ''),
            'gender': self.validated_data('gender', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(DoctorRegistrationSerializer, self).save(request)
        user.is_doctor = True
        user.phone_number = self.cleaned_data.get('phone_number')
        user.gender = self.cleaned_data.get('gender')
        user.save()
        doctor = Doctor(
            doctor = user,
            bio = self.cleaned_data.get('bio')
        )
        doctor.save()
        return user

class PatientRegistrationSerializer(RegisterSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True,)
    gender = serializers.ChoiceField(choices=User.GENDER)
    phone_number = serializers.CharField(required=True,)
    dob = serializers.DateField()
    height = serializers.FloatField()
    weight = serializers.FloatField()

    def get_cleaned_data(self):
        data = super(PatientRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'phone_number': self.validated_data('phone_number', ''),
            'gender': self.validated_data('gender', ''),
            'dob': self.validated_data('dob', ''),
            'height': self.validated_data('height', ''),
            'weight': self.validated_data('weight', '')
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(PatientRegistrationSerializer, self).save(request)
        user.is_patient = True
        user.phone_number = self.cleaned_data.get('phone_number')
        user.gender = self.cleaned_data.get('gender')
        user.save()
        patient = Patient(
            patient = user,
            dob = self.cleaned_data.get('dob'),
            height = self.cleaned_data.get('height'),
            weight = self.cleaned_data.get('weight'),
        )
        patient.save()
        return user


