"""
Views for question...dedicated to absoltue {{ value }}

Developer: Anway Somani

"""

from django.shortcuts import render, redirect
from ..models import Question, Subject, SubjectCategory
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
    question_2 = Question.objects.filter(block=id, marks=2)#.order_by('?')[:2]
    question_5 = Question.objects.filter(block=id, marks=5)
    question_10 = Question.objects.filter(block=id, marks=10)
 
    subjects = Subject.objects.all()

    initial_data = {
            'block': id
    }
    form = QuestionForm(request.POST or None, initial=initial_data)

    # Form for question creation
    if request.method=="POST":
        if form.is_valid():
            form.save()
            question = form.cleaned_data['question']
            marks = form.cleaned_data['marks']
            if marks is 2:
                print("Value taken up here")
            print("Saved Question")
    else:
        form = QuestionForm(initial=initial_data)
        print("Status unclarified...")

    context = {
               'form': form,
               'list': lister,
               'object': obj,
               'id': id,
               '2mksques': question_2,
               '5mksques': question_5,
               '10mksques': question_10,
               'subjects': subjects,
    }

    return render(request, "faculty/question.html", context)

# ------------------------------------------------------------------------
# Generic Views: Manipulating existing data

# Update Question(View)
class QuestionUpdate(UpdateView):
    model = Question
    fields = ['block', 'modules', 'question', 'marks', 'priority', 'notes']
    template_name = 'faculty/questindex/questionedit.html'
    success_url = '#'

# Delete Question(View)
class QuestionDelete(DeleteView):
    #import ipdb; ipdb.set_trace()
    model = Question
    template_name = 'faculty/question.html'
    success_url = '#'

from django.shortcuts import get_object_or_404

# Deleting single question input
def Questiondelete(request, id):
    user = request.user
    obj = get_object_or_404(Question, id=id)
    context = {
               'id': obj.id,
    }
    if request.method == "GET":
        obj.delete()
        return render(request, "faculty/questindex/questiondel.html")

    return render(request, "faculty/questindex/questiondel.html", context)





