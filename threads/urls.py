from django.urls import path
from . import views

urlpatterns = [
    path('', views.Threads.as_view(), name='threads'),
    path('<int:thId>/', views.SingleThread.as_view(), name='thread'),
    path('newThread', views.NewThread.as_view(), name='newThread'),
    path('random/', views.RandomThread.as_view(), name='random_thread'),
    path('edit_thread/<int:thId>/', views.EditThreadView.as_view(), name='edit_thread'),
    path('delete_thread/<int:thId>/', views.DeleteThread.as_view(), name='delete_thread'),
    path('like_thread/<int:thId>/', views.like_thread, name='like_thread'),
    path('like_comment/<int:thId>/', views.like_comment, name='like_comment'),
]