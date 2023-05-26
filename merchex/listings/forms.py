from django import forms
from django.forms import ModelForm
from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandForm(ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        