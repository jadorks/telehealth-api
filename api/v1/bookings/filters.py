import django_filters
from .models import AppointmentSlot, Booking
from django_filters import rest_framework as filters


class SlotFilter(filters.FilterSet):
    start_gte = django_filters.DateTimeFilter(field_name="start_time", lookup_expr="gte")
    start_lte = django_filters.DateTimeFilter(field_name="start_time", lookup_expr="lte")
    doctor = django_filters.NumberFilter(field_name="doctor__id", lookup_expr='iexact')
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    
    class Meta:
        model = AppointmentSlot
        fields = ['start_gte', 'start_lte', 'doctor', 'status']

class BookingFilter(filters.FilterSet):
    patient = django_filters.NumberFilter(field_name="patient__id", lookup_expr='iexact')
    status = django_filters.CharFilter(field_name="booking_status", lookup_expr='iexact')

    class Meta:
        model = Booking
        fields = ['patient']

