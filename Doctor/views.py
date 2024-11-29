from django.shortcuts import render,redirect
from Patient.models import*
from Patient.forms import*

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required(login_url="/")
def DoctorPage(request):
    return render(request,"doctor.html")

@login_required(login_url="/")
def userAppoinments(request,doc_id,pat_id):
    doctor = doctorModels.objects.get(id = doc_id)
    patient = appoinmentModels.objects.get(id = pat_id)
    doctor.patients.add(patient)

    context = {
        'doctor' :doctor,
        'patient':patient
    }
    return render(request,"viewapp.html",context)



@login_required(login_url="/")
def view_appointments(request):
    appointments = Appointments.objects.all()
    context = {
        "appointments": appointments,
    }
    return render(request, "viewapp.html", context)
