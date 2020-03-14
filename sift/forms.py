from django import forms 
from .models import im

class imForm(forms.Form):
    imform=forms.ImageField()
    cropform=forms.ImageField()