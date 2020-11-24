from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserFrom
from django.db import IntegrityError
# Create your views here.

def home(request):
    return render(request, 'home.html', {"title":"Home"})

def myregister(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        try:
            uname = request.POST.get('username')
            f_name = request.POST.get('first_name')
            l_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            user = User.objects.create_user(username=uname, first_name=f_name, last_name=l_name, email=email, password=password)
            return redirect('/login')
        except IntegrityError as e:
            print(e)
    form = CreateUserFrom()
    return render(request, 'registration.html',{"title":"Register","form":form})

def mylogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username != "" and password != "":
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                return redirect('/')
    return render(request, 'login.html',{"title":"Login"})

def mylogout(request):
    logout(request)
    return redirect('/login')