from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    