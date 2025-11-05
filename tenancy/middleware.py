

from hotels.models import Hotel


class ActiveHotelMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response
        
    
    def __call__(self,request):
        hotel_id=request.session.get('active_hotel_id')
        
        if hotel_id:
            try:
                request.active_hotel=Hotel.objects.get(id=hotel_id)
            except Hotel.DoesNotExist:
                request.active_hotel=None
        else:
            request.active_hotel=None
        
        return self.get_response(request)