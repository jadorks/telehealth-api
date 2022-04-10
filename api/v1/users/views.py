from django.shortcuts import render
from api.v1.users.serializers import DoctorRegistrationSerializer, PatientRegistrationSerializer
from dj_rest_auth.registration.views import RegisterView

# Create your views here.
class DoctorRegisterView(RegisterView):
    serializer_class = DoctorRegistrationSerializer

class PatientRegisterView(RegisterView):
    serializer_class = PatientRegistrationSerializer