from django.shortcuts import redirect
from django.urls import reverse


class CustomerMiddleware:
    
    def __init__(self,get_response) -> None:
        self.get_response = get_response
        
    def __call__(self,request) :
        user = request.user
        
        if not user.is_authenticated:
            return redirect(reverse('accounts:login'))
        
        if user.role and user.role.name != "admin":
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
        return self.get_response(request)
        