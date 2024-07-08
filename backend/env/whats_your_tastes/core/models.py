from django.db import models

# Create your models here.
# Class for User
class User (models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)