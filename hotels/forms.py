from django import forms
from hotels.models import Hotel


class EmployeeCreationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=255)
 
class HotelCreationForm(forms.ModelForm):
     name=forms.CharField(max_length=50, required=True,
                          widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel name"}))
     email=forms.CharField(max_length=50, required=True,
                          widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel email"}))
     address = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel address"}))
     city = forms.CharField(max_length=150, required=True,
                            widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel city"}))
     phone_number = forms.CharField(max_length=20, required=False,
                                    widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel phone number"}))
     description = forms.CharField(required=False,
                                   widget=forms.Textarea(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel description","style":"height: 100px"}))
     hotel_profile = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={"class":"d-none","placeholder":"Enter Hotel description","id":"hotelLogo"}))
     
     class Meta:
         model=Hotel
         fields = ['name', 'address', 'email','phone_number','city', 'description', 'hotel_profile']