from django.shortcuts import render
from api.v1.users.models import Doctor, Patient
from api.v1.users.serializers import DoctorRegistrationSerializer, DoctorSerializer, PatientRegistrationSerializer, PatientSerializer
from dj_rest_auth.registration.views import RegisterView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView, Response

# Create your views here.
class DoctorRegisterView(RegisterView):
    serializer_class = DoctorRegistrationSerializer

class PatientRegisterView(RegisterView):
    serializer_class = PatientRegistrationSerializer

class DoctorListView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientListView(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRetrieveView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class CurrentPatientView(APIView):
    def get(self, request):
        user = request.user.id
        patient = Patient.objects.get(patient=user)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

