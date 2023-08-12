from django.http import HttpResponseNotFound
from django.shortcuts import render
from threads.models import *
from django.views.generic import ListView

class ATW_Home(ListView):
    model = Thread
    template_name = 'main/main.html'
    context_object_name = 'threads'

def pageNotFound(request, exception):
    return render(request, 'main/pageNotFound.html')