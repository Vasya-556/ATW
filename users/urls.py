from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('profile', views.user_view, name='user'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', RegisterUser.as_view(), name='signup'),
]
