from django.shortcuts import redirect
from .models import Hotel

class ActiveHotelRequiredMixin:
    
    def dispatch(self,request,*args,**kwargs):
        hotel_id=request.session.get("active_hotel_id")
        
        if not hotel_id:
            return redirect("managerpanel:hotels_list")
        
        try:
            request.active_hotel=Hotel.objects.get(id=hotel_id,manager=request.user)
            
        except Hotel.DoesNotExist:
            return redirect("managerpanel:hotels_list")
        
        return super().dispatch(request,*args,**kwargs)