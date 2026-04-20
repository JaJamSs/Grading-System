from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Redirect root URL to dashboard
@login_required(login_url='login')
def home(request):
    return redirect('dashboard_test')  # Automatically go to dashboard

@login_required(login_url='login')
def dashboard_test_view(request):
    return render(request, 'core/dashboard_test.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_test')  # Send user directly to dashboard

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_test')  # After login → dashboard
        else:
            return render(request, 'core/login.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    # Always redirect after logout, regardless of GET or POST
    return redirect('login')