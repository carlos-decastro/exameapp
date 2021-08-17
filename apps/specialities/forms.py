from django import forms
from .models import Speciality

class SpecialityForm(forms.ModelForm):

    class Meta:
        model = Speciality
        exclude = ('created_on' , 'updated_on',)