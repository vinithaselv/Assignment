from django.forms import ModelForm
from  .models import *

# class patientform(ModelForm):
#      class Meta:
#           model = patientModels
#           fields ="__all__"

class appoinmentform(ModelForm):
     class Meta:
          model = appoinmentModels
          fields = ['pat_name', 'specialization', 'doc_name', 'date', 'time']