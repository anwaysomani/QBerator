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

