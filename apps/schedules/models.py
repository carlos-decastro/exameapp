from django.db import models
from patients.models import Patient
from locales.models import Locale
 
# Create your models here.

class Scheduling(models.Model):
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField('Data', auto_now=False, auto_now_add=False)
    hour = models.CharField('Horario', max_length=5)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    locale = models.ForeignKey(Locale, on_delete=models.CASCADE)
    
    STATUS_CHOICES = (
        ('Agendado', 'Agendado'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Agendado')

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
        ordering =['-id']

    def _str_(self):
        return self.date
