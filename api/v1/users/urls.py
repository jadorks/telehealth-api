from django.urls import path, re_path
from .views import CurrentPatientView, DoctorListView, DoctorRegisterView, DoctorRetrieveView, PatientListView, PatientRegisterView, PatientRetrieveView
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView



urlpatterns = [

    # registration urls
    path('doctors/register', DoctorRegisterView.as_view(), name='register-doctor'),
    path('patients/register', PatientRegisterView.as_view(), name='register-patient'),

    # login and logout urls
    path('patients/login', LoginView.as_view()),
    path('patients/logout', LogoutView.as_view()),

    # account confirmation urls
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
         VerifyEmailView.as_view(), name='account_confirm_email'),

    # list and retrieve urls
    path('doctors', DoctorListView.as_view(), name='list-doctor'),
    path('doctors/<int:pk>', DoctorRetrieveView.as_view(), name='retrieve-doctor'),
    path('patients', PatientListView.as_view(), name='list-patient'),
    path('patients/<int:pk>', PatientRetrieveView.as_view(), name='retrieve-patient'),
    path('current_patient', CurrentPatientView.as_view(), name='current-patient')
]