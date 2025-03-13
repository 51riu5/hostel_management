from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as authlogout, login as authlogin ,authenticate
from django.contrib.auth.decorators import login_required

def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username=username,email=email,password=password) 
        except Exception as e:  
            error_message=str(e)
    return render(request, "userlogin.html",{"user":user,"error_message":error_message})

def login(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            authlogin(request,user)
            return redirect('profile')
        else:
            error_message="Invalid credentials"
    return render(request, "login.html",{"user":user,"error_message":error_message})

@login_required
def profile(request):
    return render(request, "profile.html")
