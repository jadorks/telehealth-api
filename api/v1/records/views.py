from django.shortcuts import render
from .models import MedicalRecord, RecordItem
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import RecordItemSerializer, RecordSerializer

# Create your views here.
class RecordList(ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = RecordSerializer

class RecordDetail(RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = RecordSerializer

class RecordItemList(ListCreateAPIView):
    queryset = RecordItem.objects.all()
    serializer_class = RecordItemSerializer

class RecordItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = RecordItem.objects.all()
    serializer_class = RecordItemSerializer