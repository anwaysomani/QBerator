from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import InsQuestion

class InsQuestionListView(ListView):
    model =  InsQuestion
    context_object_name = 'question'

class InsQuestionCreateView(CreateView):
    model = InsQuestion
    fields = ('branch', 'specialization', 'semester', 'course', 'module', 'chapter', 'question', 'marks', 'priority', 'note')
    success_url = reverse_lazy('question_changelist')

class InsQuestionUpdateView(UpdateView):
    model = InsQuestion
    fields = ('branch', 'specialization', 'semester', 'course', 'module', 'chapter', 'question', 'marks', 'priority', 'note')
    success_url = reverse_lazy('question_changelist')

