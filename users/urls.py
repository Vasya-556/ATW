from django.urls import path
from . import views
from .views import RegisterUser
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('my_profile', views.user, name='user'),
    # path('login', views.user_login, name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('signup', views.signup, name='signup'),
    path('signup/', RegisterUser.as_view(), name='signup'),
]
