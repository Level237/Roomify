from django.shortcuts import render
from hotels.forms import EmployeeCreationForm
from hotels.models import Hotelier
from roles.models import Role
from .model import Hotel
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.http import HttpResponseForbidden
from django.core.mail import send_mail
# Create your views here.

User = get_user_model()

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
            role_id=Role.objects.get(name="hotelier").id,
        )
        
        Hotelier.objects.create(
            user=user,
            hotel=hotel,
        )
        
        send_mail(
            subject=f"Account Hotelier form {hotel.name}",
            message=f"Hello {data['username']},\n\n"
                    f"You have been added as a hotel employee\n\n"
                    f"Your temporary password is: {temp_password}\n\n"
                    f"Please log in to change your password with this link http://example.com/employee/set-password/{user.id}\n\n"
                    f"Thank you for using Roomify.\n\n"
                    f"Roomify Team",
            from_email="Roomify <roomify@roomify.com>",
            recipient_list=[user.email],
        )