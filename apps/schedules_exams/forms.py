from django import forms
from .models import SchedulingExam, Exam, Scheduling, Doctor

class SchedulingExamForm(forms.ModelForm):
    
    class Meta:
        model = SchedulingExam
        exclude = ('scheduling', 'created_on' , 'updated_on')