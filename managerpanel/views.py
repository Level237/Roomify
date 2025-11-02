from accounts.utils import account_activation_token
from core.utils import get_base_url
from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from hotels.forms import EmployeeCreationForm
from hotels.models import Hotel,Hotelier
# Create your views here.
from django.http import HttpResponseForbidden
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from roles.models import Role


User = get_user_model()
def dashboard_manager(request):
    show_hotel_form = request.GET.get('r')
    
    if show_hotel_form == 'new-hotel':
        show_hotel_form = True
    else:
        show_hotel_form = False
    return render(request,"manager/dashboard.html",{'show_hotel_form':show_hotel_form})

def switch_hotel(request,hotel_id):
    hotel= get_object_or_404(Hotel,id=hotel_id,manager=request.user)
    request.session['active_hotel_id'] = hotel.id
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
        
       
    
