from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'message': f'Hello {request.user.username}'})
    else:
        return render(request, 'home.html', {'message': 'Hello Stranger'})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'User created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Username already exists')
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('home')