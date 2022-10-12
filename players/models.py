from django.db import models

# Create your models here.
class PlayerList(models.Model):
    userid = models.IntegerField(null=True)
    firstname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    value = models.IntegerField()
    