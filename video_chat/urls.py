from django.urls import path
from .views import JoinRoom, RoomView
from .utils import end_room

app_name = 'video_chat'
urlpatterns = [
    path('join/<str:ref>', JoinRoom.as_view(), name="join-room"),
    path('room/<str:room_name>', RoomView.as_view(), name="room-view"),
    path('end_room/<room_sid>', end_room, name="end-room")
]