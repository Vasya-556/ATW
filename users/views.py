from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView
from .models import *
from .forms import *

class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'  

    def get_success_url(self) -> str:
        return reverse_lazy('main')

class RegisterUser(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def user_view(request):
    return render(request, 'users/user.html')

def logout_user(request):
    logout(request)
    return redirect('login')