from django.db import models
from hotels.models import Hotel

# Create your models here.

class Room(models.Model):
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name="rooms")
    room_number= models.CharField(max_length=50)
    room_type=models.CharField(max_length=100)
    price_per_night=models.DecimalField(max_digits=10, decimal_places=2)
    is_available=models.BooleanField(default=True)
    capacity= models.IntegerField(default=1)
    room_profile= models.ImageField(upload_to='rooms/profiles/',blank=True,null=False)
    def __str_(self):
        return f"{self.hotel.name} - {self.room_number}"
    

class RoomImage(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="galery_rooms")
    image=models.ImageField(upload_to="rooms/galery/",blank=True,null=True)
    
    def __str__(self):
        return f"galery image for {self.room}"
