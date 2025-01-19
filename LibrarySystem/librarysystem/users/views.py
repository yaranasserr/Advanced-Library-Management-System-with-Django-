from django.shortcuts import render
from django.http import HttpResponse
from users.forms import InputForm


def home(request):
    return render(request, 'home.html')


def form_view(request):
    form = InputForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = InputForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')