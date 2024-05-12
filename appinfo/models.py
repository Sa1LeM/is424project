from django.db import models

class Account(models.Model):
    username= models.CharField(max_length=64)
    password= models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phoneNum = models.IntegerField()