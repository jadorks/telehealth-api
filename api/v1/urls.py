from django.urls import path, include

urlpatterns = [
    path('bookings/', include('api.v1.bookings.urls'))
]