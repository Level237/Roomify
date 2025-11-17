from django.db import models
from django.conf import settings
import uuid
from decimal import Decimal
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
    country = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    phone_number =models.CharField(max_length=255,blank=True,null=True)
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
    

def upload_to_profile(instance,filename):
    return f"hotels/{instance.room.hotel.id}/rooms/{instance.id}/profile/{filename}"

def upload_to_galery(instance,filename):
    return f"hotels/{instance.room.hotel.id}/rooms/{instance.id}/galery/{filename}" 
class Room(models.Model):
    room_id=models.CharField(primary_key=True,max_length=50,editable=False,unique=True),
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="rooms")
    room_number= models.CharField(max_length=50)
    room_type=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True),
    room_type = models.CharField(max_length=100, choices=[
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
        ('family', 'Family'),
        ('vip', 'VIP'),
    ]),
    price_per_night=models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    is_available=models.BooleanField(default=True)
    capacity= models.PositiveIntegerField(default=1)
    room_profile= models.ImageField(upload_to=upload_to_profile,blank=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def save(self,*args,**kwargs):
        if not self.room_id:
            from django_tenants.utils import get_tenant
            
            tenant=get_tenant()
            hotel_slug=tenant.name[:6]
            random_part=uuid.uuid4().hex[:6]
            self.room_id= f"{hotel_slug}-{random_part}"
        super().save(*args,**kwargs)
        

    def __str__(self):
        return f"{self.hotel.name} - {self.room_number}"
    

class RoomImage(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="galery_images")
    image=models.ImageField(upload_to=upload_to_galery,blank=True,null=True)
    upload_at=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return f"galery image for {self.room}"
    

    
