from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import User

def user_login(request):
    return render(request, 'users/login.html')

def signup(request):
    if request.method == 'POST':
        # Отримуємо дані з форми
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        dob = request.POST['dob']
        gender = request.POST['gender']
        
        # Перевірка, чи паролі співпадають
        if password != password_repeat:
            # Якщо паролі не співпадають, можна відобразити помилку або зробити інше відповідне повідомлення користувачеві
            return render(request, 'users/signup.html', {'error': 'Passwords do not match'})
        
        # Створення нового користувача
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Збереження додаткових даних користувача
        user.dob = dob
        user.gender = gender
        user.save()
        
        # Перенаправлення користувача на сторінку після успішної реєстрації
        return redirect('main')
    
    return render(request, 'users/signup.html')