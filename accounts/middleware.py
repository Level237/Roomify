from django.shortcuts import redirect
from django.urls import reverse


class RoleRequiredMiddleware:
    
    def __init__(self,get_response) -> None:
        self.get_response = get_response
        
    def __call__(self,request) :
        user = request.user
        
        if not user.is_authenticated:
            return redirect('accounts:login')
        
        if user.role and user.role.name != "manager":
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
        