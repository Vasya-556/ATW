from django.db import models
from django.contrib.auth.models import User
from users.models import *
from django.urls import reverse

class Rating(models.Model):
    VOTE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )

    TYPE_CHOICES = (
        ('Thread', 'Thread'),
        ('Comment', 'Comment'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    liked_object_id = models.PositiveIntegerField()
    liked_object_type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    like_type = models.CharField(max_length=7, choices=VOTE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.like_type} - {self.liked_object_type} - {self.liked_object_id}"

    class Meta:
        unique_together = ('user', 'liked_object_id', 'liked_object_type')

class Thread(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=250)
    time_create = models.DateTimeField('Time of publication',auto_now_add=True)
    time_update = models.DateTimeField('Time of update',auto_now=True)
    full_text = models.TextField('Full text')

    ratings = models.ManyToManyField(Rating, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['time_create', 'title']
    
class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Comment')
    time_create = models.DateTimeField('Created_at', auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    ratings = models.ManyToManyField(Rating, blank=True)

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        ordering = ['-time_create']