from django.shortcuts import render
from hotels.forms import EmployeeCreationForm, HotelStepOneAddress, HotelStepOneFile, HotelStepOneInformation
from django.urls import reverse
from django.shortcuts import redirect
from hotels.models import Hotel
from django.contrib import messages
from django.contrib.auth.models import User
from django_tenants.utils import schema_context
from tenants.models import Domain, HotelTenant
import uuid
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
                form=HotelStepOneAddress(request.POST or None)
                if request.method=="POST" and form.is_valid():
                    request.session['hotel_step_one_address']=form.cleaned_data
                    return redirect(f"{reverse('public:signup')}?s=1&i=file")
            elif i=="file":
                form=HotelStepOneFile(request.POST or None)
                if request.method=="POST" and form.is_valid():
                        request.session['hotel_step_one_file'] = {
                        'color': form.cleaned_data['color'],
                        'hotel_profile_name': form.cleaned_data['hotel_profile'].name,
                    }
                        request.session['hotel_profile'] = form.cleaned_data['hotel_profile']
                        return redirect(f"{reverse('public:signup')}?s=2")
        elif step == "2":
            form=EmployeeCreationForm(request.POST or None)
            if request.method=="POST" and form.is_valid():
                return redirect(f"{reverse('public:signup')}?s=3")
        elif not step:
            return redirect(f"{reverse('public:signup')}?s=1&i=infos")
        return render(request, 'public/auth/signup.html',{'form': form,"step":step,"i":i})

def public_home_view(request):
    return render(request, 'public/Homepage.html')

def store_hotel(request):
    try:
        infos=request.session.get('hotel_step_one_infos')
        address=request.session.get('hotel_step_one_address')
        file=request.session.get('hotel_step_one_file')
        employee=request.session.get('hotel_step_two')
        
        if not all([infos,address,file,employee]):
            messages.error(request,"Missing data")
            return redirect(f"{reverse('public:signup')}")
        
        user=User.objects.create_user(
            username=employee['username'],
            email=employee['email'],
            password=employee['password'],
        )
        
        tenant=HotelTenant.objects.create(
            name=infos['name'],
            schema_name=infos['name'].lower().replace(" ","_")
        )
        
        domain=Domain.objects.create(
            domaine=f"{tenant.schema_name}.localhost",
            tenant=tenant,
            is_primary=True
        )
        
        with schema_context(tenant.schema_name):
            hotel=Hotel.objects.create(
                id=uuid.uuid4(),
                owner=user,
                name=infos['name'],
                email=infos['email'],
                address=address['address'],
                city=address['city'],
                country=address['country'],
                phone_number=employee['phone_number'],
                description=infos['description'],
                hotel_profile=request.session.get('hotel_profile'),
                color=file['color'],
            )
            
            for key in ['hotel_step_one_infos','hotel_step_one_address','hotel_step_one_file','hotel_step_two']:
                request.session.pop(key, None)
                
            messages.success(request,f"Hotel {infos['name']} created successfully")
            return redirect(f"https://{domain.domain}:8000/dashboard")
    except Exception as e:
        messages.error(request,str(e))
        return redirect(reverse('public:signup'))