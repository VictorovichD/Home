from django import forms
from.models import *
class GuysFoms(forms.ModelForm):
    class Meta:
        model = Guys
        exclude = ['']
