from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
import random
from django.db.models import Count

class Threads(ListView):
    paginate_by = 10
    model = Thread
    template_name = 'threads/threads.html'
    context_object_name = 'threads'

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', '-time_create')
        search_text = self.request.GET.get('search_text', '')

        if search_text:
            return Thread.objects.filter(Q(title__icontains=search_text) | Q(full_text__icontains=search_text) | Q(author__username__icontains=search_text)).order_by(order_by)

        return Thread.objects.order_by(order_by).select_related('author')

class SingleThread(DetailView):
    model = Thread
    template_name = 'threads/thread.html'
    context_object_name = 'thread'
    pk_url_kwarg = 'thId'

    def get_queryset(self):
        return Thread.objects.order_by().prefetch_related('ratings', 'comments__ratings', 'comments__author').select_related('author')

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddNewComment()

        context['likes'] = Rating.objects.filter(
            liked_object_id=self.object.pk,
            liked_object_type='Thread',
            like_type='like',
        ).count()
        context['dislikes'] = Rating.objects.filter(
            liked_object_id=self.object.pk,
            liked_object_type='Thread',
            like_type='dislike',
        ).count()

        comment_ratings = Rating.objects.filter(
            liked_object_type='Comment',
            like_type='like',
            liked_object_id__in=self.object.comments.all(),
        ).values('liked_object_id').annotate(like_count=Count('liked_object_id'))

        context['comment_likes'] = {rating['liked_object_id']: rating['like_count'] for rating in comment_ratings}

        comment_dislikes = Rating.objects.filter(
            liked_object_type='Comment',
            like_type='dislike',
            liked_object_id__in=self.object.comments.all(),
        ).values('liked_object_id').annotate(dislike_count=Count('liked_object_id'))

        context['comment_dislikes'] = {rating['liked_object_id']: rating['dislike_count'] for rating in comment_dislikes}

        return context
        
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

    def get_queryset(self):
        return Thread.objects.order_by().select_related('author')

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

class RandomThread(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        all_threads = Thread.objects.all()

        random_thread = random.choice(all_threads)

        return reverse('thread', args=[random_thread.pk])
    
def like_thread(request, thId):
    thread = get_object_or_404(Thread, pk=thId)
    like_type = request.POST.get('like_type')

    if like_type not in ['like', 'dislike']:
        return redirect('thread', thId=thread.pk)

    rating, created = Rating.objects.get_or_create(
        user=request.user,
        liked_object_id=thread.pk,
        liked_object_type='Thread',
        defaults={'like_type': like_type}
    )

    if not created:
        rating.like_type = like_type
        rating.save()

    return redirect('thread', thId=thread.pk)

def like_comment(request, thId):
    thread = get_object_or_404(Thread, pk=thId)
    like_type = request.POST.get('like_type')
    comment_id = request.POST.get('comment_id')

    if like_type not in ['like', 'dislike']:
        return redirect('thread', thId=thread.pk)

    comment = get_object_or_404(Comment, pk=comment_id)

    rating, created = Rating.objects.get_or_create(
        user=request.user,
        liked_object_id=comment.pk,
        liked_object_type='Comment',
        defaults={'like_type': like_type}
    )

    if not created:
        rating.like_type = like_type
        rating.save()

    return redirect('thread', thId=thread.pk)

class EditCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'threads/thread.html'  
    form_class = EditCommentForm
    context_object_name = 'comment'
    pk_url_kwarg = 'commentId'

    def get_success_url(self):
        thId = self.kwargs['thId']
        return reverse_lazy('thread', kwargs={'thId': thId})

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()

        if not request.user.is_authenticated or request.user != comment.author:
            return redirect('main')

        return super().dispatch(request, *args, **kwargs)
    
class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'threads/thread.html'  
    context_object_name = 'comment'
    pk_url_kwarg = 'commentId'

    def get_success_url(self):
        thId = self.kwargs['thId']
        return reverse('thread', kwargs={'thId': thId})

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()

        if not request.user.is_authenticated or request.user != comment.author:
            return redirect('main')

        return super().dispatch(request, *args, **kwargs)