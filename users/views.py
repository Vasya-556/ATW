from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request, 'users/user.html')

def login(request):
    return render(request, 'users/login.html')