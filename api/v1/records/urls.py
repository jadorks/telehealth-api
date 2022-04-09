from django.urls import path
from .views import RecordList, RecordDetail, RecordItemList, RecordItemDetail

urlpatterns = [
    path('', RecordList.as_view(), name='record-list'),
    path('<int:pk>', RecordDetail.as_view(), name='record-detail'),
    path('items', RecordItemList.as_view(), name='items-list'),
    path('items/<int:pk>', RecordItemDetail.as_view(), name='items-detail')
]