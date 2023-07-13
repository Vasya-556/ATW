from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def user(request):
    return render(request, 'users/user.html')

def login(request):
    if request.method == 'POST':
        data = request.POST
        email = data['email']
        nickname = data['nickname']
        password = data['password']
        dob = data['dob']
        sex = data['sex']

        # Perform additional checks and database operations
        # Check if the email or nickname already exists in the database
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists.'}, status=400)

        if User.objects.filter(nickname=nickname).exists():
            return JsonResponse({'error': 'Nickname already exists.'}, status=400)

        # Create a new User instance
        user = User(email=email, nickname=nickname, password=password, dob=dob, sex=sex)
        user.save()

        # Return a success response
        return JsonResponse({'message': 'User created successfully!'})

    return render(request, 'users/login.html')