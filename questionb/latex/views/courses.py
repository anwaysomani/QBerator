from django.shortcuts import render, redirect
from ..forms import QuestionForm

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

