from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import JsonResponse

class Threads(ListView):
    paginate_by = 5
    model = Thread
    template_name = 'threads/threads.html'
    context_object_name = 'threads'

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', '-time_create')
        return Thread.objects.order_by(order_by)

class SingleThread(DetailView):
    model = Thread
    template_name = 'threads/thread.html'
    context_object_name = 'thread'
    pk_url_kwarg = 'thId'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddNewComment()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AddNewComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = self.object
            comment.author = request.user
            comment.save()
            return redirect('thread', thId=self.object.pk)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        
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
    
class DeleteThread(DeleteView):
    model = Thread
    template_name = 'threads/delete_thread.html'
    success_url = reverse_lazy('threads')
    pk_url_kwarg = 'thId'
