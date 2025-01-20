from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm , InputForm , ProfileForm

from .models import Profile

def home(request):
    return render(request, 'home.html')


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'


    def form_valid(self, form):
        user = form.save()  # Save the user instance
        login(self.request, user)  # Log the user in immediately after signing up
        return redirect('dashboard')





def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse('Invalid credentials')
    else:
        form = InputForm()  # Ensure the form is passed here
        return render(request, 'login.html', {'form': form})
    
def logout_user(request):
    logout(request)
    return redirect('home')
    
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html', {'first_name': request.user.first_name})

@login_required
def profile_view(request):
    # Get or create the user's profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})