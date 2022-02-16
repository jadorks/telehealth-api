from django.urls import path
from .views import BookingList, BookingDetail, SlotList, SlotDetail

urlpatterns = [
    path('', BookingList.as_view(), name='booking-list'),
    path('<int:pk>', BookingDetail.as_view(), name='booking-detail'),
    path('slots', SlotList.as_view(), name='slot-list'),
    path('slots/<int:pk>', SlotDetail.as_view(), name='slot-list')
]