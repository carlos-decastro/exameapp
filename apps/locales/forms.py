from django import forms
from .models import Locale

class LocaleForm(forms.ModelForm):

    class Meta:
        model = Locale
        exclude = ('created_on' , 'updated_on',)