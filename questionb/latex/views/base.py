from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from ..models import *
from ..forms import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Creating redirection page
def main(request):
    return render(request, 'main.html', {})

# Faculty Login View
def faculty_login(request):
    print(request.user.is_authenticated())
    title = "Faculty Login"
    form = FacultyLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('findex')

    return render(request, "registration/facultylogin.html", {"form":form, "title":title})


# HoD Login View
def hod_login(request):
    print(request.user.is_authenticated())
    title = "Department Head Login"
    form = HODLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('hindex')

    return render(request, "registration/hodlogin.html", {"form":form, "title":title})


# Post-Faculty Login
def findex(request):
    return render(request, 'faculty/findex.html', {})

def hindex(request):
    return render(request, 'hod/hindex.html', {})



