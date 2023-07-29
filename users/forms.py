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
    gender = forms.ChoiceField(label='Sex', choices=SEX_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-input'}))
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = CustomUser 
        fields = ('username','password1','password2','gender','date_of_birth','email')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-input'}))


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','gender','avatar','additional_info']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-input'}, choices=SEX_CHOICES),
            'avatar': forms.FileInput(attrs={'class': 'form-input'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
        }