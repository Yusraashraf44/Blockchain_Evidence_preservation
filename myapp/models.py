from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    photo = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)

class Complaint(models.Model):
    date=models.DateField()
    sendcomplaint= models.CharField(max_length=1000)
    reply = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)



