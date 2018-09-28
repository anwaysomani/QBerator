from django.shortcuts import render, redirect
from ..models import *
from ..forms import *

def save_question(request):
    form = QuestionForm(request.POST)
    if form.is_valid:
        form.save(commit=True)
