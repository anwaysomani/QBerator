"""
It contains the following views:

- View for the main page, which enables on clicking the link to the server block. It is the main link, and can be called as :8000/main

- View for the faculty login page, link to which is :8000/flogin. It isnt a neccesity to go the main page. Someone with the link can use to directly access the faculty login page.

- View for the hod login page, link to which is :8000/hlogin. It has the same specs as the faculty login, i.e, someone with the linnk can use to directly access the hod login page.

- View for faculty post-login page(findex).

- View for hod post-login page(hindex).

Developer: Anway Somani

"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from ..models import Subject

# Creating main page...redirecting after
def main(request):
    return render(request, 'main.html')
# -----------------------------------------

# Post-Faculty Login
def findex(request):
    user = request.user
    lister = user.profile.subjects.all()
    ider = user.profile.subjects.all()
    
    context = {
               'list': lister,
               'user': user,
               'id': ider,
    }

    return render(request, 'faculty/findex.html', context)

# Post-Head-of-Department Login
def hindex(request):
    subjects = Subject.objects.all()

    context = {
               'subject': subjects,
    }
    return render(request, 'hod/hindex.html', context)


def error(request):
    return render(request, 'error.html')

