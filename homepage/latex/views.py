from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'base.html')


# index page of faculty containing view option and all accordions
def facultyindex(request):
    return render(request, 'index/faculty_index.html', {})

def facultysem1index(request):
    return render(request, 'faculty/index/index_sem1.html', {})

def facultysem2index(request):
    return render(request, 'faculty/index/index_sem2.html', {})

def facultysem3index(request):
    return render(request, 'faculty/index/index_sem3.html', {})

def facultysem4index(request):
    return render(request, 'faculty/index/index_sem4.html', {})

def facultysem5index(request):
    return render(request, 'faculty/index/index_sem5.html', {})

def facultysem6index(request):
    return render(request, 'faculty/index/index_sem6.html', {})

def facultysem7index(request):
    return render(request, 'faculty/index/index_sem7.html', {})

def facultysem8index(request):
    return render(request, 'faculty/index/index_sem8.html', {})


# BCA - MACT modal view
from django.views.generic import ListView
from fm.views import AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from .models import EI
from .form import EIForm

class English_I_ListView(ListView):
    model = EI

class English_I_CreateView(AjaxCreateView):
    form_class = EIForm

# bal: to create update and delete view for English_I
