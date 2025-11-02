from django.shortcuts import redirect
from django.urls import reverse

class ActivateHotelMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_authenticated and request.user.role.name == "manager":
            hotel_id = request.session.get('active_hotel_id')
            if not hotel_id and request.path.startswith('/manager/'):
                return redirect(reverse('manager:dashboard'))
                
        return self.get_response(request)
        