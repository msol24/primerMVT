from django.db import models
from datetime import date

# Create your models here.

class Pariente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    parentesco = models.CharField(max_length=40)
    edad = models.IntegerField()
    