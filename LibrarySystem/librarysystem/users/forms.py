from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)

    
  