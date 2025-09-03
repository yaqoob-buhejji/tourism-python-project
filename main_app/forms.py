from django import forms
from .models import Place

class PlaceForm (forms.ModelForm):
    class Meta :
        model = Place
        fields = ["name","location","information","review","imgs"]
        