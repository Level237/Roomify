from django.db import models
from django.contrib.auth.models import AbstractUser
from roles.models import Role
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,null=True,blank=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []
    def __str__(self) -> str:
        return f"{self.email} - {self.role.name if self.role else "Nothing"}"