from django.contrib import admin
from .models import Room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel','room_number','room_type','price_per_night','is_available','capacity','room_profile')
    
admin.site.register(Room,RoomAdmin)
