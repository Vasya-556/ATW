from django.db import models
import datetime

class User(models.Model):
    nickname = models.CharField('Nickname', max_length=20)
    login = models.CharField('Login', max_length=20, default='login')
    password = models.CharField('Password', max_length=20, default='password')
    sex = models.CharField('Sex', max_length=10, default='none')
    date = models.DateField('Date of Registration')
    about = models.CharField('About', max_length=250)
    photo = models.ImageField('Photo', upload_to='user_photos/')
    dob = models.DateField('Date of birth', default=datetime.date(2012, 12, 12).strftime('%Y-%m-%d'))