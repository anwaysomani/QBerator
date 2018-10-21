from django.shortcuts import render, redirect
from ..models import *
from ..forms import *
from django.contrib.auth.decorators import login_required

# Redirect for subject-page

@login_required(login_url='/accounts/login/')
def quesdata_view(request):
    #obj = Subject.objects.get(id=1)
    
    # Form for question creation
    form = QuestionForm()

    return render(request, "faculty/question.html", {'form': form})
