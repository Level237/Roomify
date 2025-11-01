from django.db import models
from django.conf import settings

# Create your models here.

class Hotel(models.Model):
    manager=models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              limit_choices_to={'role__name': 'manager'},
                              related_name="hotels"
                              )
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
    

    
