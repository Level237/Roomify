from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.base import File
from decimal import Decimal

from hotels.widget import MultipleFileInput
class EmployeeCreationForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter username"}))
    email = forms.CharField(max_length=255,widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter confirm password"}))
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class HotelStepOneInformation(forms.Form):
    name=forms.CharField(max_length=50, required=True,
                          widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel name"}))
    email=forms.CharField(max_length=50, required=True,
                          widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel email"}))
    phone_number = forms.CharField(max_length=20, required=False,
                                    widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel phone number"}))
    description = forms.CharField(required=False,
                                   widget=forms.Textarea(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel description","style":"height: 100px"}))

class HotelStepOneAddress(forms.Form):
    address = forms.CharField(max_length=255, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel address"}))
    city = forms.CharField(max_length=150, required=True,
                           widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel city"}))
    country = forms.CharField(max_length=150, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel country"}))

        
class HotelStepOneFile(forms.Form):
    hotel_profile = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={"class":"form-control","placeholder":"Enter Hotel description","id":"hotel_profile"}))
    color=forms.CharField(max_length=7, required=True,
                          widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Hotel color",'type':'color','style':"height:50px"}))

class TenantLoginForm(AuthenticationForm):
    username=forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Enter a username'
        })
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class':"form-control",
            'placeholder':"Enter a password"
        })
    )
    

class CreateRoomForm(forms.Form):
    
    room_number=forms.CharField(max_length=50, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter room number"}))
    size_m2=forms.IntegerField(min_value=0, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter room size in m2"}))
    beds=forms.IntegerField(min_value=1, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter room beds"}))
    room_type=forms.CharField(max_length=100, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter room type"}))
    description=forms.CharField(required=False,
                                   widget=forms.Textarea(attrs={"class":"form-control form-control-modern","placeholder":"Enter room description","style":"height: 100px"}))
    price_per_night=forms.DecimalField(max_digits=10, decimal_places=2, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter room price per night"}))
    is_available=forms.BooleanField(required=True,
                              widget=forms.CheckboxInput(attrs={"class":"form-check-input"}))
    capacity = forms.IntegerField(min_value=1, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter room capacity"}))
    room_profile = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={"class":"form-control","placeholder":"Enter room description","id":"room_profile"}))

    images = forms.FileField(required=False, widget=MultipleFileInput(attrs={"class":"form-control","placeholder":"Enter room description","id":"id_images","multiple":True, "accept": "image/*",}))


class ForgotPassword(forms.Form):
    
    email=forms.EmailField(required=True,
                           widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your email"}))