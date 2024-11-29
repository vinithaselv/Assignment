from django.db import models
from django.conf import settings

# Create your models here.
# class patientModels(models.Model):
#     patient_name = models.TextField()
#     last_name = models.TextField()
#     gender = models.TextField()
#     pat_password = models.TextField()
#     pat_password_confirm = models.TextField(null=True)
#     phoneno = models.TextField()

#     def __str__(self):
#         return self.patient_name



class appoinmentModels(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    pat_name = models.CharField(max_length=100,null=True)
    specialization = models.CharField(max_length=100)
    doc_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Appointment for {self.pat_name} with Dr. {self.doc_name} on {self.date} at {self.time}"

