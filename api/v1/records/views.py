from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from api.v1.records.filters import RecordFilter
from api.v1.users.models import Patient

from .models import RecordItem
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import RecordItemListSerializer, RecordItemSerializer

# Create your views here.
class RecordItemList(ListCreateAPIView):
    queryset = RecordItem.objects.all()
    serializer_class = RecordItemSerializer
    filter_class = RecordFilter

    def list(self, request):
        queryset = RecordItem.objects.filter(patient__id=self.request.query_params.get('patient')) if self.request.query_params.get('patient') else RecordItem.objects.all()
        serializer = RecordItemListSerializer(queryset, many=True, context={"request":request})
        return Response(serializer.data)

class RecordItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = RecordItem.objects.all()
    serializer_class = RecordItemSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecordItemListSerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        patient = get_object_or_404(Patient, patient=self.request.user.id)
        serializer.save(patient=patient)