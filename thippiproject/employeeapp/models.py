from django.db import models

# Create your models here.
class employee(models.Model):
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    salary = models.FloatField()
    email = models.CharField(max_length=35)