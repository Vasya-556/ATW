from django.urls import path
from . import views

urlpatterns = [
    path('', views.Threads.as_view(), name='threads'),
    path('<int:thId>/', views.SingleThread.as_view(), name='thread'),
    path('newThread', views.NewThread.as_view(), name='newThread'),
]