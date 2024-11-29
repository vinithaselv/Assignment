from django.urls import path
from .views import *


urlpatterns = [
    path('patient/',patientPage,name="patient"),
    path('bookappoinments/',bookapoinment,name='bookappinments'),
    path('my/appoinment/',myappoinment,name ='myappoinment'),
    path('update/appoinment/<int:id>/',updateappoinment,name='update'),
    path('delete/appoinment/<int:id>/',deletedata,name='delete')
]