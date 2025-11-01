from django.shortcuts import render

# Create your views here.


def dashboard_manager(request):
    return render(request,"manager/dashboard.html")
