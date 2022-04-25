import django_filters
from django_filters import rest_framework as filters

from api.v1.records.models import RecordItem


class RecordFilter(filters.FilterSet):
    patient = django_filters.NumberFilter(field_name="patient__id", lookup_expr='iexact')

    class Meta:
        model = RecordItem
        fields = ['patient']