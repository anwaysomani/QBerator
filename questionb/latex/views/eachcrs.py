from django.shortcuts import render, redirect
from ..models import *
from ..forms import *
from django.contrib.auth.decorators import login_required

# Redirect for subject-page

@login_required(login_url='/accounts/login/')
def quesdata_view(request, id):
    user = request.user    
    lister = user.profile.subject.all()
    obj = Subject.objects.filter(id=id)

    # Form for question creation
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            #form.save(commit=False)
            question = form.cleaned_data['question']
            modules = form.cleaned_data['modules']
            marks = form.cleaned_data['marks']
            priority = form.cleaned_data['priority']
            notes = form.cleaned_data['notes']
            form.save()
            print("Saved Question")
    else:
        form = QuestionForm()
        print("Cannot get form saved")

    query = Question.objects.filter()

    return render(request, "faculty/question.html", {'form': form, 'query': query, 'list': lister, 'object': obj, 'id': id})

"""
def subjdata_view(request):
    #user = request.user
    #obje = user.profile.subject.all()#id=subject.id)
    lister = user.profile.subject.all()
    
    context = {
               'list': lister,
               'object': obje,
               #'id': id,
               'user': user
              }
    return render(request, "faculty/question.html", context)
"""

