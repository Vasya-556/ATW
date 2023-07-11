from django.urls import path
from . import views

urlpatterns = [
    path('my_profile', views.user, name='user'),
    path('', views.login, name='login'),
]
