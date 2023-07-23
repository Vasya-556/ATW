from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView

# def AllThreads(request):
#     threads = Thread.objects.all()
#     return render(request, 'threads/threads.html', {'threads': threads})

class Threads(ListView):
    model = Thread
    template_name = 'threads/threads.html'
    context_object_name = 'threads'

class SingleThread(DetailView):
    model = Thread
    template_name = 'threads/thread.html'
    context_object_name = 'thread'
    pk_url_kwarg = 'thId'

class NewThread(CreateView):
    form_class = AddNewThread
    template_name = 'threads/NewThread.html'
    success_url = reverse_lazy('threads')


# def Thread_(request, thId):
#     thread = get_object_or_404(Thread, id=thId)
#     return render(request, 'threads/thread.html', {'thread': thread})

# def NewThread(request):
#     if request.method == 'POST':
#         form = AddNewThread(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect ('main')
#     else:
#         form = AddNewThread()
#     return render(request, 'threads/NewThread.html', {'form': form})