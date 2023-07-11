from django.shortcuts import render
from .models import Thread

def index(request):
    threads = Thread.objects.all()
    return render(request, 'threads/threads.html',{'threads': threads})