from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()