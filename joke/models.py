from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class usuario(models.Model):
    usuarios = models.CharField(max_length=30, primary_key=True)
    contraseña = models.CharField(max_length=30)