from django.shortcuts import render
from .forms import InsQuestion 
from django.urls import reverse

def index(request):
    return render(request, 'base.html')

def form(request):
    return render(request, 'form.html', {'form': InsQuestion()})

def list(request):
    return render(request, 'list.html')
