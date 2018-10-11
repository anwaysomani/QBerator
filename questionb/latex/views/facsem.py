from django.shortcuts import render, redirect
from ..models import *
from ..forms import *

# Sidenavbar views for extended html's

# Semester-1
def sem1(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
  
        if form.is_valid():
            form.save()
            #all_questions = AQuestion.objects.all
            #return render(request, 'faculty/exfindex/sem3.html', {'form': form})
            
    else:
        form = QuestionForm()
    return render(request, 'faculty/exfindex/sem1.html', {'form': form})

# Semester-2
def sem2(request):
    return render(request, 'faculty/exfindex/sem2.html', {})

# Semester-3
def sem3(request):
    return render(request, 'faculty/exfindex/sem3.html', {})

# Semester-4
def sem4(request):
    return render(request, 'faculty/exfindex/sem4.html', {})

# Semester-5
def sem5(request):
    return render(request, 'faculty/exfindex/sem5.html', {})

# Semester-6
def sem6(request):
    return render(request, 'faculty/exfindex/sem6.html', {})

# Semester-7
def sem7(request):
    return render(request, 'faculty/exfindex/sem7.html', {})

# Semester-8
def sem8(request):
    return render(request, 'faculty/exfindex/sem8.html', {})
