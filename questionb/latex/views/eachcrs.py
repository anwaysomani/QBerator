"""
Views for question...dedicated to absoltue {{ value }}

Developer: Anway Somani

"""

from django.shortcuts import render, redirect
from ..models import Question, Subject
from ..forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# Page: QuestionCreate,+QuestionList
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
            #block = id
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
        print("Status unclarified...")

    context = {
               'form': form,
               'query': query,
               'list': lister,
               'object': obj,
               'id': id,
    }

    return render(request, "faculty/question.html", context)

# ------------------------------------------------------------------------
# Generic Views: Manipulating existing data

# Update Question(View)
class QuestionUpdate(UpdateView):
    model = Question
    fields = ['block', 'modules', 'question', 'marks', 'priority', 'notes']
    template_name = 'faculty/questindex/questionedit.html'
    success_url = '#'  #reverse_lazy('question-update')

# Delete Question(View)
class QuestionDelete(DeleteView):
    model = Question
    template_name = 'faculty/questindex/questiondel.html'
    success_url = 'eachsubject'

