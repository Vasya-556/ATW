from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('id','username','registration_date')

admin.site.register(CustomUser, CustomUserAdmin)