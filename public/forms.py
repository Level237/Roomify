from django import forms
class TenantSignupHotelForm(forms.Form):
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
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        address = cleaned_data.get("address")
        city = cleaned_data.get("city")
        phone_number = cleaned_data.get("phone_number")
        description = cleaned_data.get("description")
        hotel_profile = cleaned_data.get("hotel_profile")
        
        if not name or not email or not address or not city or not phone_number or not description or not hotel_profile:
            raise forms.ValidationError("All fields are required")
        
        return cleaned_data