from django import forms
from phonenumber_field.formfields import PhoneNumberField # NOUVEL IMPORT
from django_countries.fields import CountryField   

class EmployeeCreationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
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
    phone_number =  PhoneNumberField(max_length=20, required=False,
                                    widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel phone number"}, help_text="Format international requis (ex: +33 6 12 34 56 78)."))
    description = forms.CharField(required=False,
                                   widget=forms.Textarea(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel description","style":"height: 100px"}))

class HotelStepOneAddress(forms.Form):
    address = forms.CharField(max_length=255, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel address"}))
    city = forms.CharField(max_length=150, required=True,
                           widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel city"}))
    country = CountryField().formfield(max_length=150, required=True,
                              widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel country"}))
    
class HotelStepOneFile(forms.Form):
    hotel_profile = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={"class":"d-none","placeholder":"Enter Hotel description","id":"hotelLogo"}))
    

