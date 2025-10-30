from  django import forms
from    .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,get_user_model

class CustomRegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter your password'}))
    confirm_password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter your confirm password'}))
    
    class Meta:
        model= CustomUser
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
    

class CustomLoginForm(forms.Form):
    
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
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.user_cache=None
        

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get('email')
        password = cleaned.get('password')
        print(email)
        if email and password:
            # Option A: si tu as un backend personnalisé qui accepte email kwarg:
            user = authenticate(self.request, email=email, password=password)
            print("level")
            # Option B: si tu n'as PAS de backend email, mais user.email unique :
            # try:
            #     u = User.objects.get(email=email)
            # except User.DoesNotExist:
            #     raise forms.ValidationError("Aucun compte ne correspond à cet email.")
            # user = authenticate(self.request, username=u.username, password=password)

            if user is None:
                raise forms.ValidationError("Identifiants invalides.")
            if not user.is_active:
                raise forms.ValidationError("Ce compte est inactif.")
            self.user_cache = user

        return cleaned

    def get_user(self):
        return self.user_cache

    
    