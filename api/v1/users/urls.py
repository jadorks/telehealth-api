from django.urls import path

from .views import DoctorRegisterView, PatientRegisterView

urlpatterns = [
    path('doctors/register', DoctorRegisterView.as_view(), name='register-doctor'),
    path('patients/register', PatientRegisterView.as_view(), name='register-patient')
]