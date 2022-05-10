from django.http import response
from rest_framework.response import Response

from api.v1.users.models import Patient
from .filters import BookingFilter, SlotFilter
from django.shortcuts import get_object_or_404, render
from .models import AppointmentSlot, Booking
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookingSerializer, SlotSerializer, BookingListSerializer

# Create your views here.

class BookingList(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_class = BookingFilter

    def list(self, request):
        queryset = Booking.objects.filter(patient__id=self.request.query_params.get('patient')).filter(booking_status=self.request.query_params.get('status')) if self.request.query_params.get('patient') and self.request.query_params.get('status') else Booking.objects.all()
        serializer = BookingListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        patient = get_object_or_404(Patient, patient=self.request.user.id)
        serializer.save(patient=patient)

class BookingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookingListSerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        patient = get_object_or_404(Patient, patient=self.request.user.id)
        serializer.save(patient=patient)

class SlotList(ListCreateAPIView):
    queryset = AppointmentSlot.objects.all()
    serializer_class = SlotSerializer
    filter_class = SlotFilter

class SlotDetail(RetrieveUpdateDestroyAPIView):
    queryset = AppointmentSlot.objects.all()
    serializer_class = SlotSerializer