

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from hotels.models import Hotel, Room
from django.contrib.auth import authenticate, login
from .forms import TenantLoginForm,CreateRoomForm,ForgotPasswordForm
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
# Create your views here.


def tenant_login(request):
    
    if request.user.is_authenticated:
        return redirect('hotels:dashboard')
    
    form=TenantLoginForm(request,data=request.POST or None)
    message=""
    if request.method == "POST" and form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('hotels:dashboard')
        else:
            message = 'Nom d’utilisateur ou mot de passe incorrect.'
            
    return render(request, 'hotels/auth/login.html', {'form': form, 'message': message})

@login_required
def dashboard(request):
    try:
        hotel=Hotel.objects.get(owner=request.user)
    except Hotel.DoesNotExist:
        hotel=None
        
    context={
        "hotel":hotel,
        "tenant_schema":request.tenant.schema_name,
    }
    
    
    return render(request, 'hotels/dashboard.html',context)


@login_required

def room_list(request):
    show_modal=request.GET.get('r') == 'new-room'
    room_form=CreateRoomForm()
    rooms=Room.objects.all()
    
    if request.method == "POST":
        room_form=CreateRoomForm(request.POST,request.FILES)
        
        if room_form.is_valid():
            
            with transaction.atomic():
                
                room=Room.objects.create(
                    hotel=request.user.hotel,
                    room_number=room_form.cleaned_data['room_number'],
                    size_m2=room_form.cleaned_data['size_m2'],
                    beds=room_form.cleaned_data['beds'],
                    room_type=room_form.cleaned_data['room_type'],
                    description=room_form.cleaned_data['description'],
                    price_per_night=room_form.cleaned_data['price_per_night'],
                    is_available=room_form.cleaned_data['is_available'],
                    capacity=room_form.cleaned_data['capacity'],
                    room_profile=room_form.cleaned_data['room_profile']
                )
                
                images=request.FILES.getlist('images')
                
                for image in images:
                    RoomImage.objects.create(
                        room=room,
                        image=image
                    )
                
                return redirect('hotels:manage-rooms')
        
    return render(request,'hotels/rooms/room-list.html',{'rooms':rooms,'show_modal':show_modal,'room_form':room_form})


def forgot_password(request):
    form=ForgotPasswordForm()
    
    if request.method == 'POST':
        form=ForgotPasswordForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            try:
                user=User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request,"This email does not exist")
                return redirect('hotels:forgot-password')
            uuid=urlsafe_base64_encode(force_bytes(user.pk))
            token=token_generator.make_token(user)
            
            reset_link=request.build_absolute_uri(
                f"/reset/{uuid}/{token}/"
            )
            
            send_mail(
                subject="Reset your password",
                message=f"Click the link to reset your password:\n\n{reset_link}",
                from_email="Roomify <roomify@roomify.com>",
                recipient_list=[email],
            )
            
            messages.success(request, "A password reset link has been sent to your email.")
            
            return redirect('hotels:forgot-password')
    return render(request,"hotels/auth/forgot-password.html",{'form':form})
    