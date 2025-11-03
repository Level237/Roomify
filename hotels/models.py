from django.db import models
from django.conf import settings
import shortuuid

# Create your models here.

def generate_short_uuid():
    return shortuuid.uuid()[:10]
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
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    description= models.TextField(blank=True,null=True)
    hotel_profile=models.ImageField(upload_to='hotels/profiles/',blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Hotelier(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="hotelier")
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    
    hired_date =models.DateField(auto_now_add=True)
    
    def _str_(self):
        return f"{self.user.username} - {self.hotel.name}"
    

    
