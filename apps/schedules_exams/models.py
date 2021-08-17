from django.db import models
from schedules.models import Scheduling
from exams.models import Exam
from doctors.models import Doctor
 
# Create your models here.

class SchedulingExam(models.Model):
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    scheduling = models.ForeignKey(Scheduling, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Agenda de Exame'
        verbose_name_plural = 'Agendas de Exames'
        ordering =['id']

    def _str_(self):
        return self.doctor
