from django.shortcuts import render
from .forms import CreateQuestion

def CreateQuest(request):
    if request.method == 'POST':
        form = CreateQuestion(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateQuestion()

    return render(request, 'faculty/createquestion.html', {'form': form})


def index(request):
    return render(request, 'base.html')

import simplejson
from django.https import HttpResponse

def get_specialization(request, branch_id):
    branch = models.Branch.objects.get(pk=branch_id)
    specializations = models.Specialization.filter(branch=branch)
    specialization_dict = {}
    for specialization in specializations:
        specialization_dict[specialization.id] = specialization.name
    return HttpResponse(simplejson.dumps(specialization_dict), mimetype="application/json")
