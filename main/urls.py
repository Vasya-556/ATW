from django.urls import path
from . import views

urlpatterns = [
    path('', views.ATW_Home.as_view(), name='main'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
