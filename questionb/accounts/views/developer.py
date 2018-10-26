from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView


# Views for different developer-side optionnaires
def AboutDeveloper(request):
    return render(request, 'developer/developerinfo.html', {})

