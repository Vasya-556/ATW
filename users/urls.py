from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', RegisterUser.as_view(), name='signup'),
]
