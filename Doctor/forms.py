from django.forms import ModelForm
from  .models import *

class doctorform(ModelForm):
    class Meta:
         model = doctorModels
         fields = "__all__"

class  Appoinments(ModelForm):
     class Meta:
          model =  Appointments
          fields = "__all__"
