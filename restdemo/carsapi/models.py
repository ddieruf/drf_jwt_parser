from django.db import models
from authentication.models import User

class Car(models.Model):
    userid = models.IntegerField(default=None)
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    price = models.IntegerField()
