from django import forms
from .models import Profile  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
 
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class InputForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['street_address', 'city', 'state_province', 'postal_code', 'country']  # Only these fields are visible to the user

    def save(self, commit=True):
      
        profile = super().save(commit=False)
        
        if commit:
            profile.save()
       
        profile.update_location()
        
        return profile