from django.db import models
from django.contrib.auth.models import User
from users.models import *
from django.urls import reverse

class Thread(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='threads')
    title = models.CharField('Title', max_length=250)
    time_create = models.DateTimeField('Time of publication',auto_now_add=True)
    time_update = models.DateTimeField('Time of update',auto_now=True)
    full_text = models.TextField('Full text')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['time_create', 'title']
    
class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Comment_text')
    time_create = models.DateTimeField('Created_at', auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['time_create']