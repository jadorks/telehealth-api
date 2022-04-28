from django import forms

class VideoForm(forms.Form):
    participant = forms.EmailField()