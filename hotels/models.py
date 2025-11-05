from django.db import models
from django.conf import settings
import shortuuid
from tenancy.manager import TenantManager
from tenancy.models import TenantBaseModal

# Create your models here.

def generate_short_uuid():
    return shortuuid.uuid()[:10]

def upload_to(instance,filename):
    return f"hotels/profiles/{instance.id}/{filename}"
class Hotel(models.Model):
    
    id=models.CharField(max_length=15,primary_key=True,default=generate_short_uuid,editable=False)
    manager=models.ForeignKey(settings.AUTH_USER_MODEL,
                              to_field="id",
                              on_delete=models.CASCADE,
                              limit_choices_to={'role__name': 'manager'},
                              related_name="hotels"
                              )
    is_active=models.BooleanField(default=False)
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length=50,null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    description= models.TextField(blank=True,null=True)
    hotel_profile=models.ImageField(upload_to=upload_to,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    
class Hotelier(TenantBaseModal):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="hotelier")
    
    hired_date =models.DateField(auto_now_add=True)
    
    objects= TenantManager()
    def _str_(self):
        return f"{self.user.username} - {self.hotel.name}"
    

    
