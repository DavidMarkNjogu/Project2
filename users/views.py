from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomUserCreationForm, CustomLoginForm, CustomSignupForm

# Signup view to handle user registration
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  #Create the user
            backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user, backend=backend)  # Log the user in
            messages.success(request, 'Signup successful.')
            return redirect('home') # Redirect to home or another page
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

# Custom password change view extending PasswordChangeView
class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account_change_password_done')
    template_name = 'account/password_change.html'

# Login view to handle user authentication
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()
    return render(request, 'account/login.html', {'form': form})

# Logout view to handle user logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')
