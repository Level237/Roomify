from .forms import CustomRegisterForm,CustomLoginForm
from django.shortcuts import render,redirect
from django.contrib.auth import login

def register_user(request):
    if request.method == "POST":
        form= CustomRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('core:home')
    else:
        form=CustomRegisterForm()
    return render(request,'accounts/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form=CustomLoginForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('core:home')
    else:
        form =CustomLoginForm()
    return render(request,'accounts/login.html',{'form':form})
            
        
