from django.contrib import admin
from .models import *

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create')
    list_display_links = ('id','title')
    search_fields = ('title','full_text')
    list_filter = ('time_create',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','thread','time_create')
    list_display_links = ('id','thread')
    search_fields = ('id','text')


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)