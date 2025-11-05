from django.db import models

class TenantManager(models.Manager):
    
    def for_request(self,request):
        hotel=getattr(request,'active_hotel',None)
        
        if hotel:
            return self.filter(hotel=hotel)
        
        return self.none()