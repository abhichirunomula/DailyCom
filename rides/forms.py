from django import forms
from .models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['source', 'destination', 'date', 'seats_available', 'price']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }