from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from threads.models import *
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from .forms import *

class ATW_Home(ListView):
    model = Thread
    template_name = 'main/main.html'
    context_object_name = 'threads'

    def get_queryset(self):
        return Thread.objects.select_related('author')

def pageNotFound(request, exception):
    return render(request, 'main/pageNotFound.html')

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'main/contact.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('main')