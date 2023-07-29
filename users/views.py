from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from .models import *
from .forms import *
from django.contrib.auth.models import User

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


def profile(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    return render(request, 'users/profile.html', {'user': user})

def edit_profile(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    return render(request, 'users/edit_profile.html', {'user': user})

def delete_profile(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    return render(request, 'users/delete_profile.html', {'user': user})

def logout_user(request):
    logout(request)
    return redirect('login')


class EditProfileView(UpdateView):
    model = CustomUser
    template_name = 'users/edit_profile.html'
    form_class = EditProfileForm
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse_lazy('profile')