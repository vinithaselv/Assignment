from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def UserLogin(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['username'],password = request.POST['password'])

        if user is not None:
            login(request,user)
            if user.role == 1:
                return redirect('doctorPage')
            elif user.role == 2:
                return redirect('patient')
            # elif user.role == 2:
            #     return redirect('doctorPage')
            else:
                return redirect("login")
    return render(request,"login.html")

def SignUp(request):
    context = {"error": ""}

    if request.method == "POST":
        user_check = User.objects.filter(username=request.POST['username'])
        if user_check.exists():
            context = {
                'error':"User Already exists"
            }
            return render(request, "register.html", context)
        else:
            newUser = User(username = request.POST['username'],first_name = request.POST['firstName'],
                        last_name = request.POST['lastName'],email = request.POST['Email'],
                        Age = request.POST['Age'],role = request.POST['role'])
            newUser.set_password(request.POST['Password'])

            newUser.save()
            return redirect('loginPage')


    return render(request, "register.html", context)

def UserLogout(request):
    logout(request)
    return render(request,"logout.html")