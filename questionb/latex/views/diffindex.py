from django.shortcuts import render
from ..models import *
from ..forms import *

# Post-Faculty login
def findex(request):
    return render(request, 'faculty/findex.html', {})

# Post-HOD login
def hindex(request):
    return render(request, 'hod/hindex.html', {})
