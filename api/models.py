from django.db import models


# Create your models here.

class Company(models.Model):

    description=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    serie=models.CharField(max_length=50)
    precio=models.PositiveIntegerField()
    cantidad=models.CharField(max_length=50)
    disponible=models.CharField(max_length=50)
    #description,marca,serie,precio,cantidad,disponible