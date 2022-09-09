from django.db import models

# Create your models here.
class UserLoginReg(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    signin = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    funds = models.IntegerField(default=100000000)
    score = models.IntegerField(default=0)
    teamname = models.CharField(max_length=255, unique=True)
