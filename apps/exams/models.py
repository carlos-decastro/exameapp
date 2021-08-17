from django.db import models

# Create your models here.

class Exam(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    price = models.FloatField('Preco', null=True, blank=True, default=0.0)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)

    
    class Meta:
        verbose_name = 'Tipo de Exame'
        verbose_name_plural = 'Tipos de Exames'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.name) 

