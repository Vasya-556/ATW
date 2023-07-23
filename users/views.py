from typing import Any, Dict
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView
from .models import *

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # Шлях до шаблону входу
    # success_url = 'main/main.html'  # URL для перенаправлення після успішного входу
    form_class = AuthenticationForm

    def form_valid(self, form):
        # Вхід користувача успішний
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        # Помилка аутентифікації користувача
        return self.render_to_response(self.get_context_data(form=form, error='Invalid login credentials'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error'] = self.kwargs.get('error')
        return context

# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
        
#         # Аутентифікація користувача
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             # Вхід користувача успішний
#             login(request, user)
#             return redirect(reverse('main'))  # Перенаправлення після успішного входу
            
#         else:
#             return render(request, 'users/login.html', {'error': 'Invalid login credentials'})
    
#     return render(request, 'users/login.html')

# def signup(request):
#     if request.method == 'POST':
#         # Отримуємо дані з форми
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password_repeat = request.POST['password_repeat']
#         dob = request.POST['dob']
#         sex = request.POST.get('sex')  # Змінена отримання значення поля
        
#         # Перевірка, чи паролі співпадають
#         if password != password_repeat:
#             # Якщо паролі не співпадають, можна відобразити помилку або зробити інше відповідне повідомлення користувачеві
#             return render(request, 'users/signup.html', {'error': 'Passwords do not match'})
        
#         # Створення нового користувача
#         user = User.objects.create_user(username=username, email=email, password_hash=password)
        
#         # Збереження додаткових даних користувача
#         user.dob = dob
#         user.sex = sex  # Змінена змінна поля
#         user.save()
        
#         # Перенаправлення користувача на сторінку після успішної реєстрації
#         return redirect(reverse('login'))
    
#     return render(request, 'users/signup.html')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


def user_view(request):
    return render(request, 'users/user.html')