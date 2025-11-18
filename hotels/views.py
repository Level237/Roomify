

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from hotels.models import Hotel, Room
from django.contrib.auth import authenticate, login
from .forms import TenantLoginForm

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
    rooms=Room.objects.all()
    return render(request,'hotels/rooms/room-list.html',{'rooms':rooms,'show_modal':show_modal})