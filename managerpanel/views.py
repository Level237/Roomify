from accounts.utils import account_activation_token
from core.utils import get_base_url
from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from hotels.forms import EmployeeCreationForm, HotelCreationForm
from hotels.models import Hotel,Hotelier
# Create your views here.
from django.http import HttpResponseForbidden
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from roles.models import Role
from rooms.models import Room
from django.contrib import messages


User = get_user_model()
def dashboard_manager(request):

    hotel_count=Hotel.objects.filter(manager=request.user).count()
    return render(request,"manager/dashboard.html",{
        'total_hotels':hotel_count
    })

def switch_hotel(request,hotel_id):
    
    if request.method == "POST":
        hotel_id=request.POST.get("hotel_id")
        hotel= get_object_or_404(Hotel,id=hotel_id,manager=request.user)
        request.session['active_hotel_id'] = hotel.id
        messages.success(request,f"Hotel {hotel.name} Switched successfully")
    return redirect('manager:dashboard')




def send_mail_from_user(user,hotel,temp_password,token,frontend_url):
    
    
    activation_url=f"{frontend_url}/accounts/set-password/{user.id}/{token}"
    send_mail(
            subject=f"Account Hotelier form {hotel.name}",
            message=f"Hello {user.username},\n\n"
                    f"You have been added as a hotel employee\n\n"
                    f"Your temporary password is: {temp_password}\n\n"
                    f"Please log in to change your password with this link {activation_url}\n\n"
                    f"Thank you for using Roomify.\n\n"
                    f"Roomify Team",
            from_email="Roomify <roomify@roomify.com>",
            recipient_list=[user.email],
        )
def create_hotel(request,hotel_id):
    hotel=Hotel.objects.get(id=hotel_id)
    
    if request.user != hotel.manager:
        return HttpResponseForbidden("Vous n'avez pas accès à ce hôtel")
    form= EmployeeCreationForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        data =form.cleaned_data
        
        temp_password= get_random_string(length=12)
        
        user= User.objects.create_user(
            username=data['username'],
            email = data['email'],
            password=temp_password,
            is_active=False,
            role_id=Role.objects.get(name="hotelier").id,
        )
        
        token=account_activation_token.make_token(user)
        Hotelier.objects.create(
            user=user,
            hotel=hotel,
        )
        frontend_url=get_base_url(request)
        send_mail_from_user(user,hotel,temp_password,token,frontend_url)
        

def hotels_list(request):
    show_hotel_form = request.GET.get('r') == 'new-hotel'
    total_hotels=Hotel.objects.filter(manager=request.user).count()
    total_hotels_is_active=Hotel.objects.filter(manager=request.user,is_active=True).count()
    total_hotels_is_not_active=Hotel.objects.filter(manager=request.user,is_active=False).count()
    
    manager=request.user
    total_rooms=Room.objects.filter(hotel__manager=manager).count()
    form = HotelCreationForm()
    hotels=Hotel.objects.filter(manager=request.user)
    if request.method == "POST" :
        form = HotelCreationForm(request.POST,request.FILES)
        
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.manager =request.user
            hotel.save()
            return redirect("managerpanel:hotels_list")
    
    return render(request,"manager/hotels/hotel-list.html",{
        'form':form,
        'show_hotel_form':show_hotel_form,
        'hotels':hotels,
        'total_hotels':total_hotels,
        'total_hotels_is_active':total_hotels_is_active,
        'total_hotels_is_not_active':total_hotels_is_not_active,
        'total_rooms' : total_rooms
    })
        
       
    
