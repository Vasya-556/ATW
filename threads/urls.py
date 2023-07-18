from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllThreads, name='threads'),
    path('<int:thId>/', views.Thread_, name='threads'),
]