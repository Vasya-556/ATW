from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

class Threads(ListView):
    paginate_by = 5
    model = Thread
    template_name = 'threads/threads.html'
    context_object_name = 'threads'

class SingleThread(DetailView):
    model = Thread
    template_name = 'threads/thread.html'
    context_object_name = 'thread'
    pk_url_kwarg = 'thId'

class NewThread(LoginRequiredMixin, CreateView):
    form_class = AddNewThread
    template_name = 'threads/NewThread.html'
    success_url = reverse_lazy('threads')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

class EditThreadView(UpdateView):
    model = Thread
    template_name = 'threads/edit_thread.html'
    form_class = EditThreadForm
    context_object_name = 'thread'
    pk_url_kwarg = 'thId'

    def get_success_url(self):
        thId = self.kwargs['thId']
        return reverse_lazy('thread', kwargs={'thId': thId})
    
    def dispatch(self, request, *args, **kwargs):
        thread = self.get_object()

        if not request.user.is_authenticated or request.user != thread.author:
            return redirect('main')

        return super().dispatch(request, *args, **kwargs)