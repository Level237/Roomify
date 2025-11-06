from django.shortcuts import render
from django.views import View
# Create your views here.

class  TenantSignupView(View):
    def get(self, request):
        return render(request, 'public/auth/signup.html')

def public_home_view(request):
    return render(request, 'public/Homepage.html')