from django.db import models

def default_avatar():
    return 'avatars/default_avatar.jpg'

class User(models.Model):
    UserName = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=20)
    Sex = models.CharField(max_length=10)
    #DOB - Date of birth
    DOB = models.DateField()
    #DOR - Date of registration
    DOR = models.DateTimeField(auto_now_add=True)
    #LLD - Last Login Date
    LLD = models.DateTimeField(auto_now=True)
    Avatar = models.ImageField(upload_to='avatars/', default=default_avatar, null=True, blank=True)
    #AD - Additional Data
    AD = models.TextField(blank=True)

    def __str__(self):
        return self.UserName
