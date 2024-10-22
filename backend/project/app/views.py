from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import SignupForm, LoginForm

def home(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

