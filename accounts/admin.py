from .models import CustomUser
from django.contrib import admin

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username','email','is_staff','role')
admin.site.register(CustomUser,AccountAdmin)
