from django.shortcuts import render
# from .models import User

# def user(request):
#     return render(request, 'users/user.html')

def login(request):
    return render(request, 'users/login.html')

def signup(request):
    return render(request, 'users/signup.html')