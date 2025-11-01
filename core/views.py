from django.shortcuts import render



def home(request):
    return render(request,"Homepage.html")

def managerRegister(request):
    return render(request,"accounts/manager-register.html")
