from django.shortcuts import render
from django.views import View
from hotels.forms import EmployeeCreationForm, HotelStepOneAddress, HotelStepOneFile, HotelStepOneInformation
from django.urls import reverse
from django.shortcuts import redirect
from django_countries.fields import CountryField
from public.utils import get_country_from_ip
# Create your views here.




def signup(request):
        step=request.GET.get("s","")
        i=request.GET.get("i","")
        if step == "1":
            if i=="infos":
                form=HotelStepOneInformation(request.POST or None)
                if request.method=="POST" and form.is_valid():
                    request.session['hotel_step_one_infos']=form.cleaned_data
                    return redirect(f"{reverse('public:signup')}?s=1&i=address")
            elif i=="address":
                country=get_country_from_ip(request)
                form=HotelStepOneAddress(initial={"country":country})
                if request.method=="POST" and form.is_valid():
                    request.session['hotel_step_one_address']=form.cleaned_data
                    return redirect(f"{reverse('public:signup')}?s=1&i=file")
            elif i=="file":
                form=HotelStepOneFile(request.POST or None)
                if request.method=="POST" and form.is_valid():
                    request.session['hotel_step_one_file']=form.cleaned_data
                    return redirect(f"{reverse('public:signup')}?s=2")
        elif step == "2":
            form=EmployeeCreationForm(request.POST or None)
            if request.method=="POST" and form.is_valid():
                return redirect(f"{reverse('public:signup')}?s=3")
        elif not step:
            return redirect(f"{reverse('public:signup')}?s=1&i=infos")
        return render(request, 'public/auth/signup.html',{'form': form,"step":step,"i":i,"country":CountryField().formfield().choices})

def public_home_view(request):
    return render(request, 'public/Homepage.html')