from django.shortcuts import render
#from .forms import CreateQuestion

#def CreateQuest(request):
#    if request.method == 'POST':
#        form = CreateQuestion(request.POST)
#        if form.is_valid():
#            form.save()
#    else:
#        form = CreateQuestion()

#    return render(request, 'faculty/createquestion.html', {'form': form})


def index(request):
    return render(request, 'base.html')

#import simplejson
#from django.https import HttpResponse

#def get_specialization(request, branch_id):
#    branch = models.Branch.objects.get(pk=branch_id)
#    specializations = models.Specialization.filter(branch=branch)
#    specialization_dict = {}
#    for specialization in specializations:
#        specialization_dict[specialization.id] = specialization.name
#    return HttpResponse(simplejson.dumps(specialization_dict), mimetype="application/json")

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
