from django.shortcuts import render
from threads.models import *
from django.views.generic import ListView


class ATW_Home(ListView):
    model = Thread
    template_name = 'main/main.html'
    context_object_name = 'threads'

# def index(request):
#     threads = Thread.objects.all()
#     return render(request, 'main/main.html', {'threads': threads})