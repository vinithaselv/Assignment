from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    Age = models.IntegerField(null=True)

    role_choice = (
        (0,'Admin'),
        (1,'Doctor'),
        (2,'Patient')
    )
    role = models.IntegerField(default=0,choices=role_choice,null=True)
