from django.shortcuts import render, redirect
from ..forms import PaperForm

def upload_paper(request):
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print("Mission accomplished!")

    else:
        form = PaperForm()

    return render(request, 'faculty/qpaper.html', {'form': form})
