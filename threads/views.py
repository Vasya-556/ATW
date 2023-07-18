from django.shortcuts import render, get_object_or_404
from .models import Thread

def AllThreads(request):
    threads = Thread.objects.all()
    return render(request, 'threads/threads.html', {'threads': threads})

def Thread_(request, thId):
    thread = get_object_or_404(Thread, id=thId)
    return render(request, 'threads/thread.html', {'thread': thread})