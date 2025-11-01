from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from roles.models import Role
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password=None,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not email:
            raise ValueError('Superuser must have an email address')
        if not username:
            raise ValueError('Superuser must have a username')

        return self.create_user(email, username, password, **extra_fields)
        
    
class CustomUser(AbstractUser,PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,null=True,blank=True)
    firstname = models.CharField(max_length=255,null=True,blank=True)
    lastname = models.CharField(max_length=255,null=True,blank=True)
    password=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()
    def __str__(self) -> str:
        return f"{self.email} - {self.role.name if self.role else "Nothing"}"