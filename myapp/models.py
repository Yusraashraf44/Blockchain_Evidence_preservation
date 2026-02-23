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
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)

class Complaint(models.Model):
    date=models.DateField()
    sendcomplaint= models.CharField(max_length=1000)
    reply = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)

class Case(models.Model):
    case_number=models.CharField(max_length=100)
    case_title=models.CharField(max_length=100)
    case_type=models.CharField(max_length=100)
    date_of_incident=models.DateField()
    case_description = models.CharField(max_length=200)
    date_filed = models.DateField()
    petitioner_name = models.CharField(max_length=100)
    petitioner_email = models.CharField(max_length=100)
    petitioner_phone = models.CharField(max_length=100)
    petitioner_place = models.CharField(max_length=100)
    petitioner_pincode = models.CharField(max_length=100)
    petitioner_district = models.CharField(max_length=100)
    petitioner_state = models.CharField(max_length=100)
    accused = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    filing_mode=models.CharField(max_length=100)
    court_name=models.CharField(max_length=100)
    judge_assigned=models.CharField(max_length=100)
    priority=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)
    case_duration_days=models.CharField(max_length=100)


class Assigncase(models.Model):
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)
    CASE=models.ForeignKey(Case,on_delete=models.CASCADE)













