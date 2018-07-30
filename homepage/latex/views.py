from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'home.html'

def about(request):
    return render(request, 'subs/about.html')

def CreateQues(request):
    return render(request, 'Questionnaire/create.html', {})
