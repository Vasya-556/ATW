from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    sex = forms.ChoiceField(label='Sex', choices=SEX_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-input'}))
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = CustomUser 
        fields = ('username','password1','password2','sex','dob','email')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    

