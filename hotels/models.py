from django.db import models
from django.conf import settings
import uuid
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



def upload_to(instance,filename):
    return f"hotels/{instance.id}/profile/{filename}"
def upload_logo(instance,filename):
    return f"hotels/{instance.id}/logo/{filename}"


class Hotel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                              to_field="id",
                             on_delete=models.CASCADE, related_name='owned_hotel')
    
    is_active=models.BooleanField(default=False)
    
    name= models.CharField(max_length=50)
    
    email=models.EmailField(max_length=50,null=True)
    address = models.CharField(max_length=255)
    country=CountryField(max_length=150,null=True,blank=True)
    city = models.CharField(max_length=150)
    phone_number = PhoneNumberField(null=True,blank=True,region=None,verbose_name="Numéro de Téléphone")
    description= models.TextField(blank=True,null=True)
    hotel_profile=models.ImageField(upload_to=upload_to,blank=True,null=True)
    color=models.CharField(max_length=7,default="#000000")
    created_at = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    
class Hotelier(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="hotelier")
    hired_date =models.DateField(auto_now_add=True)
    
    def _str_(self):
        return f"{self.user.username} - {self.hotel.name}"
    

    
