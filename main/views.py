from django.http import HttpResponseNotFound
from django.shortcuts import render
from threads.models import *
from django.views.generic import ListView

class ATW_Home(ListView):
    model = Thread
    template_name = 'main/main.html'
    context_object_name = 'threads'

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found:(</h1>')
# def index(request):
#     threads = Thread.objects.all()
#     return render(request, 'main/main.html', {'threads': threads})