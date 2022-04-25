from django.urls import path
from .views import RecordItemList, RecordItemDetail

urlpatterns = [
    path('', RecordItemList.as_view(), name='record-list'),
    path('<int:pk>', RecordItemDetail.as_view(), name='record-detail'),
]