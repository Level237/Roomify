from django.contrib import admin
from .models import Room, RoomImage

# Register your models here.

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1
    fields = ('image',)
    verbose_name = " Room Image"
    verbose_name_plural = "Galery of room"
    

class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel','room_number','room_type','price_per_night','is_available','capacity','room_profile')
    inlines = [RoomImageInline]
admin.site.register(Room,RoomAdmin)
