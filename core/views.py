from accounts.forms import ManagerRegisterStepOneForm, ManagerRegisterStepTwoForm
from accounts.models import CustomUser
from django.shortcuts import render,redirect
from django.urls import reverse



def home(request):
    return render(request,"Homepage.html")

def managerRegister(request):
    step=request.GET.get('s',"") or None
    
    if step == "1":
        form=ManagerRegisterStepOneForm(request.POST or None)
        
        if request.method == "POST" and form.is_valid():
            request.session['manager_step_one_registration']=form.cleaned_data
            return redirect(f"{reverse('core:register-manager')}?s=2")
        
    elif step == "2":
        form=ManagerRegisterStepTwoForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            step_one=request.session.get("manager_step_one_registration",{})
            step_two=form.cleaned_data
            
            CustomUser.objects.create_user(
                firstname=step_one['firstname'],
                lastname=step_one['lastname'],
                email=step_one['email'],
                username=step_two['username'],
                password=step_two['password'],
                role_id=3
            )
            
            request.session.pop("manager_step_one_registration",None)
            return redirect(f"{reverse('core:register-manager')}?s=1")
    elif not step:
        return redirect(f"{reverse('core:register-manager')}?s=1")
    return render(request,"accounts/manager-register.html",{"step":step,"form":form})
