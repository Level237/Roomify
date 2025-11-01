from .forms import CustomRegisterForm,CustomLoginForm
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

User = get_user_model()



    
def register_user(request):
    if request.method == "POST":
        form= CustomRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request,user,backend='accounts.backend.EmailBackend')
            return redirect('core:home')
    else:
        form=CustomRegisterForm()
    return render(request,'accounts/register.html', {'form': form})

def login_user(request):
    form = CustomLoginForm(request.POST or None, request=request)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        print(form.errors)
        if user:
            login(request, user,backend='accounts.backend.EmailBackend')
            role_name=user.role.name.lower() if user.role else None
            print(role_name)
            if role_name == "user":
                return redirect('customerpanel:customer_dashboard')
            if role_name == "manager":
                return redirect('managerpanel:manager_dashboard')
    return render(request, 'accounts/login.html', {'form': form})

def hotelier_set_password(request,user_id):
    user=User.objects.get(id=user_id)
    
    if request.method == "POST":
        form=SetPasswordForm(user,request.POST)
        
        if form.is_valid:
            form.save()
            
            return redirect("accounts:login")
    return render(request,"password-reset.html",{'form':form})
        

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("core:home")
            
        
