from django.db import models

# Create your models here.


class Tipo(models.Model):
    descricao = models.CharField(max_length=255)

class Item(models.Model):
    descricao = models.CharField(max_length=255)
    dataCadastro = models.DateField(null=True, blank=True)
    estoqueMinimo = models.IntegerField(blank=True, null=True)
    tipo = models.ManyToManyField(Tipo, help_text='Selecione um Tipo para este item')

