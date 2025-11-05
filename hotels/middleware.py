from django.utils.deprecation import MiddlewareMixin
from hotels.models import Hotel

class SubdomainHotelMiddleware(MiddlewareMixin):
    def process_request(self,request):
        host=request.get_host().split(':')[0]
        subdomain=host.split('.')[0]
        
        try:
            request.hotel= Hotel.objects.get(subdomain=subdomain)
            
        except Hotel.DoesNotExist:
            request.hotel=None
        