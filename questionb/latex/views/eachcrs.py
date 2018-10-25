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
    query = Question.objects.filter(block=id)
    
    # Form for question creation
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            #block = form.cleaned_data['block']
            question = form.cleaned_data['question']
            modules = form.cleaned_data['modules']
            marks = form.cleaned_data['marks']
            priority = form.cleaned_data['priority']
            notes = form.cleaned_data['notes']
            form.save()
            print("Saved Question")
            form = QuestionForm()
    else:
        form = QuestionForm()
        print("Cannot decide status...")

    return render(request, "faculty/question.html", {'form': form, 'query': query, 'list': lister, 'object': obj, 'id': id})

# ------------------------------------------------------------------------
# Generic Views

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

class QuestionUpdate(UpdateView):
    model = Question

    print("Completed updation succesfully")
    fields = ['block', 'modules', 'question', 'marks', 'priority', 'notes']
    template_name = 'faculty/questindex/questionedit.html'
    success_url = '#'  #reverse_lazy('question-update')


class QuestionDelete(DeleteView):
    model = Question
    template_name = 'faculty/questindex/questiondel.html'
    success_url = 'eachsubject'


