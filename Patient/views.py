from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
@login_required(login_url="/")
def patientPage(request):
    return render(request,"patient.html")


@login_required(login_url="/")
def bookapoinment(request):
    if request.method == "POST":
        print(request.POST)
        form = appoinmentform(request.POST)
        if form.is_valid():
            appoinment = form.save(commit=False)
            appoinment.user = request.user
            appoinment.save()
            print("Form saved")
            return redirect("patient")
        else:
            print("Form is not saved")
            print(form.errors)
    else:
        pass
    return render(request,"boapp.html")

@login_required(login_url="/")
def updateappoinment(request, id):
    update = appoinmentModels.objects.get(id = id)
    if request.method == "POST":
        updateform = appoinmentform(request.POST,instance=update)
        if updateform.is_valid():
            updateform.save()
            return redirect("patient")
        else:
           print("Form is not saved")
           print(updateform.errors) 
           return render(request, "updateappoin.html")
    else:
        context = {
            "updateform" :appoinmentform(instance=update)
        }
    return render(request,"updateappoin.html",context)




@login_required(login_url="/")
def myappoinment(request):
    
    appoinment = appoinmentModels.objects.filter(user = request.user)
    context = {
        'appoinment' :appoinment
    }
    return render(request,"myappoin.html",context)

@login_required(login_url="/")

def deletedata(request,id):
    data = appoinmentModels.objects.filter(id = id)
    data.delete()
    return render(request,"myappin.html")
