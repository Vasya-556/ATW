from django.shortcuts import render
from threads.models import Thread

def index(request):
    threads = Thread.objects.all()
    return render(request, 'main/main.html', {'threads': threads})