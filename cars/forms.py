from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('model', 'color', 'year_of_production', 'km', 'descriptions', 'price', 'picture')