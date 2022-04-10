from django.urls import path

from .views import DoctorListView, DoctorRegisterView, DoctorRetrieveView, PatientListView, PatientRegisterView, PatientRetrieveView

urlpatterns = [
    path('doctors/register', DoctorRegisterView.as_view(), name='register-doctor'),
    path('patients/register', PatientRegisterView.as_view(), name='register-patient'),








    path('doctors', DoctorListView.as_view(), name='list-doctor'),
    path('doctors/<int:pk>', DoctorRetrieveView.as_view(), name='retrieve-doctor'),
    path('patients', PatientListView.as_view(), name='list-patient'),
    path('patients/<int:pk>', PatientRetrieveView.as_view(), name='retrieve-patient')
]