from django import forms
from .models import Scheduling, Patient

class SchedulingForm(forms.ModelForm):

    class Meta:
        model = Scheduling
        exclude = ('patient', 'created_on' , 'updated_on',)        