from django.db import models
from Patient.models import *
from django.conf import settings

# Create your models here.

class doctorModels(models.Model):
    doc_name = models.TextField()
    doc_password = models.CharField(max_length=100,null=True)
    specialization = models.TextField()

class Appointments(appoinmentModels):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)