from django.urls import path
from .views import *

urlpatterns= [
    path('doctor/',DoctorPage,name = "doctorPage"),
    path('all/appoinments/',view_appointments,name='viewappoinments'),
    path('view/appoinments/<int:doc_id>/<int:pat_id>/',userAppoinments,name='userappinments'),
]