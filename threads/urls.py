from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllThreads, name='threads'),
    path('<int:thId>/', views.Thread_, name='thread'),
    path('newThread', views.NewThread, name='newThread'),
    path('newComment', views.NewThread, name='newComment'),
]