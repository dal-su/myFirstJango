from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=32)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=90)
    phone = models.CharField(max_length=32)
    message = models.CharField(max_length=1000)

