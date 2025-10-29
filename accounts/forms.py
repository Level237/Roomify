from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, get_user_model

class CustomRegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter your password'}))
    confirm_password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter your confirm password'}))
    
    class Meta:
        model= User
        fields= ['username',"email","password"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }
        
    def clean(self):
        cleaned_data=super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')
        
        if password and confirm and password != confirm:
            self.add_error("confirm_password", " Password doesn't not match")
        return cleaned_data
    

class CustomLoginForm(AuthenticationForm):
    
    email=forms.EmailField(
        label="Email address",
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Enter a email address'
        })
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class':"form-control",
            'placeholder':"Enter a password"
        })
    )
    
    def clean(self):
        email=self.cleaned_data.get("email")
        password=self.cleaned_data.get("password")
        
        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("User does not exist")
            
            user= authenticate(username=user.email,password=password)
            if user is None:
                raise forms.ValidationError("Invalid password")
            self.user_cache = user
        return self.cleaned_data
    
    