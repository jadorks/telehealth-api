from django import forms
from api.v1.records.models import RecordItem

class VideoForm(forms.Form):
    participant = forms.EmailField()

class RecordForm(forms.ModelForm):
    class Meta:
        model = RecordItem
        exclude = ['doctor', 'patient', 'booking_id']