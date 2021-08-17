from django.db import models

# Create your models here.

class Speciality(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Especilidade', max_length=50)
        
    class Meta:
        verbose_name = 'Especilidade'
        verbose_name_plural = 'Especialidades'
        ordering =['id']

    def __str__(self):
        return self.name