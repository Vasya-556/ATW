from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='threads')
    title = models.CharField('Title', max_length=250)
    time_create = models.DateTimeField('Time_of_publication',auto_now_add=True)
    time_update = models.DateTimeField('Time_of_update',auto_now=True)
    full_text = models.TextField('Full_text')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Comment_text')
    created_at = models.DateTimeField('Created_at', auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')

    def __str__(self):
        return self.text