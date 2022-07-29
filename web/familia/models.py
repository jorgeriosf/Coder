from django.db import models
from django.forms import CharField

# Create your models here.

class Integrante(models.Model):
    
    name = models.CharField(max_length=100)
    date_of_birth = CharField(max_length=10)
    age = models.IntegerField()
    description = models.CharField(max_length=200,null=True, blank=True)
    hobbies = models.CharField(max_length=200,null=True, blank=True)
