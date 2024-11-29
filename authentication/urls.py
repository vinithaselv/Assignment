from  django.urls import path
from .views import *

urlpatterns = [
    path('',UserLogin,name="loginPage"),
    path('signUp/',SignUp,name="register"),
    path('logout/',UserLogout,name='logout')
]