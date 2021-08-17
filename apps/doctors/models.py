from django.db import models
from specialities.models import Speciality

# Create your models here.

class Doctor(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    doctor_speciality = models.ManyToManyField(Speciality, through='DoctorSpeciality', blank=True)
    doc = models.FileField('Documentos', upload_to='docs')
    
    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        ordering =['id']

    def __str__(self):
        return f'%s %s' % (self.first_name, self.last_name)

class DoctorSpeciality(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Especialidade do médico'
        verbose_name_plural = 'Especialidades do médico'
        ordering =['id']

    def _str_(self):
        return self.doctor