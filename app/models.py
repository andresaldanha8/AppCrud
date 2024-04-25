from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nome = models.CharField(max_length=30)
    Endereco = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=11)