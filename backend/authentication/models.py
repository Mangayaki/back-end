from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ID = models.AutoField(primary_key=True)
    usuario =  models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha1 = models.CharField(max_length=30)
    senha2 = models.CharField(max_length=30)
    pass

class UserFav(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_manga = models.IntegerField()