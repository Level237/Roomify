from django.shortcuts import render

# Create your views here.

def dashboard_customer(request):
    return render(request,'dashboard.html')
