"""
It contains the following views:

- View for the main page, which enables on clicking the link to the server block. It is the main link, and can be called as :8000/main

- View for the faculty login page, link to which is :8000/flogin. It isnt a neccesity to go the main page. Someone with the link can use to directly access the faculty login page.

- View for the hod login page, link to which is :8000/hlogin. It has the same specs as the faculty login, i.e, someone with the linnk can use to directly access the hod login page.

- View for faculty post-login page(findex).

- View for hod post-login page(hindex).
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from ..models import *
from ..forms import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from ..constants import *

# Views below: v

# Creating main page...redirecting after
def main(request):
    return render(request, 'main.html', {})
# -----------------------------------------

# -------------------
# Post-Faculty Login:
# -------------------

# Faculty Logged-In
def findex(request):
    #import ipdb;ipdb.set_trace()
    return render(request, 'faculty/findex.html')

# Head-of-Department Logged-In
def hindex(request):
    return render(request, 'hod/hindex.html', {})

def error(request):
    return render(request, 'error.html', {})
