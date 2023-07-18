from django.db import models
#add rating for thread and comment 
class Thread(models.Model):
    title = models.CharField('Title', max_length=250)
    date = models.DateTimeField('Date_of_publication')
    full_text = models.TextField('Full_text')

    def __str__(self):
        return self.title
class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Comment_text')
    created_at = models.DateTimeField('Created_at', auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return self.text