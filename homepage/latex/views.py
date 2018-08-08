from django.shortcuts import render
from .forms import InsQuestion 

def index(request):
    return render(request, 'base.html', {'form': InsQuestion()})
