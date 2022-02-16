from django.http import response
from rest_framework.response import Response
from bookings.filters import SlotFilter
from django.shortcuts import render
from .models import AppointmentSlot, Booking
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookingSerializer, SlotSerializer, BookingListSerializer
from .models import Booking


# Create your views here.

class BookingList(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookingListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookingListSerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class SlotList(ListCreateAPIView):
    queryset = AppointmentSlot.objects.all()
    serializer_class = SlotSerializer
    filter_class = SlotFilter

class SlotDetail(RetrieveUpdateDestroyAPIView):
    queryset = AppointmentSlot.objects.all()
    serializer_class = SlotSerializer