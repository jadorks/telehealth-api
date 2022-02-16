import django_filters
from .models import AppointmentSlot
from django_filters import rest_framework as filters


class SlotFilter(filters.FilterSet):
    start_gte = django_filters.DateTimeFilter(field_name="start_time", lookup_expr="gte")
    start_lte = django_filters.DateTimeFilter(field_name="start_time", lookup_expr="lte")
    class Meta:
        model = AppointmentSlot
        fields = ['start_gte', 'start_lte']

