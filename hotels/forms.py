from django import forms


class EmployeeCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=255)
    