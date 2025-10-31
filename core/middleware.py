from django.shortcuts import redirect

class NotAuthenticatedMiddleware:
    
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request) :
        
        if request.path.endswith('/login/') or request.path.endswith('/register/'):
            user=request.user
            
            if user.is_authenticated:
                previous_url = getattr(request, 'META', {}) or {}
                previous_url = previous_url.get('HTTP_REFERER', '/')
                return redirect(previous_url)
        return self.get_response(request)