from django.urls import path
from . import views

urlpatterns = [
    # path('my_profile', views.user, name='user'),
    path('login', views.user_login, name='login'),
    path('signup', views.signup, name='signup'),
]
