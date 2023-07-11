from django.db import models

class User(models.Model):
    nickname = models.CharField('Nickname', max_length=20)
    date = models.DateField('Date of Registration')
    about = models.CharField('About', max_length=250)
    photo = models.ImageField('Photo', upload_to='user_photos/')