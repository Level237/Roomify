from django.db import models
from django.conf import settings

# Create your models here.

class Hotels(models.Model):
    manager=models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              limit_choices_to={'role': 'manager'},
                              related_name="hotels"
                              )
    name= models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    description= models.TextField(blank=True,null=True)
    hotel_profile=models.ImageField(upload_to='hotels/profiles/',blank=True,null=True)
