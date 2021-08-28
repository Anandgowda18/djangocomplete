from django.db import models

# Create your models here.
class Project(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()
    name = models.CharField(max_length=15)
    assignedto = models.CharField(max_length=15)
    priority = models.IntegerField()