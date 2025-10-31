from django.shortcuts import redirect
from django.urls import reverse


class CustomerMiddleware:
    
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request) :
        
        if request.path.startswith('/customer/'):
            user = request.user
            
            if not user.is_authenticated:
                return redirect(reverse('accounts:login'))
            
            if user.role and user.role.name != "user":
                previous_url = getattr(request, 'META', {}) or {}
                previous_url = previous_url.get('HTTP_REFERER', '/')
                return redirect(previous_url)
        return self.get_response(request)
        