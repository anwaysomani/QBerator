from django.shortcuts import render, redirect
from ..forms import QuestionForm

def RATII(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            #module = forms.cleaned_data['module']
            #question = form.cleaned_data['question']
            #marks = form.cleaned_data['marks']
            #priority = form.cleaned_data['priority']
            #notes = form.cleaned_data['notes']

            #ques = AQuestion(course='BCA-MACT', semester='3', module=module, question=question, marks=marks, priority=priority, notes=notes)
            #ques.save()

            #return HttpResponseRedirect('/')
            pass
    else:
        form = QuestionForm()

    return render(request, 'faculty/courses/BCAMACT/sem3/RATII.html', {'form': form})


def trial(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
 
        if form.is_valid():
            pass
             #form.save()
             #all_questions = AQuestion.objects.all
             #return render(request, 'faculty/exfindex/sem3.html', {'form': form})
 
    else:
        form = QuestionForm()

    return render(request, 'faculty/courses/Mock/trial.html', {'form': form})

def trial2(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
 
        if form.is_valid():
            pass
 
    else:
        form = QuestionForm()
    return render(request, 'faculty/courses/Mock/trial2.html', {'form': form})

