from django import forms


class EmployeeCreationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=255)
 
class HotelCreationForm(forms.Form):
     name=forms.CharField(max_length=50, required=True,
                          widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel name"}))
     address = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel address"}))
     city = forms.CharField(max_length=150, required=True,
                            widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel city"}))
     country = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel country"}))
     phone_number = forms.CharField(max_length=20, required=False,
                                    widget=forms.TextInput(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel phone number"}))
     description = forms.CharField(required=False,
                                   widget=forms.Textarea(attrs={"class":"form-control form-control-modern","placeholder":"Enter Hotel description"}))
     hotel_profile = forms.ImageField(required=True)
     