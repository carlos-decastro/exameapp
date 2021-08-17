from django.db import models

# Create your models here.

class Locale(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'
        ordering =['id']

    def __str__(self):
        return self.address