from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import *

# Creating redirection page
def main(request):
    return render(request, 'main.html', {})

# Faculty Login
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
    return render(request, "registration/facultylogin.html", {"form":form, "title":title})

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
    return render(request, "registration/hodlogin.html", {"form":form, "title":title})


# Second view for checking authentication(login form)
"""
def faculty_login(request):
    title = "Faculty Login"

    if request.method == 'POST':
        form = faculty_login(data=request.POST)
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=email, password=password)
        if form.is_valid():
            auth.login(request, user)
            user_type = form.cleaned_data['Label']
            if user.is_active & user_type == 'Faculty':
                return HttpResponseRedirect('/findex/')
            elif user_type == 'Hod':
                return HttpResponseRedirect('/hindex/')
    #else:
        #form = faculty_login()

    return render(request, 'registration/facultylogin.html', {'form': form})
"""





# Post-Faculty Login
def findex(request):
    return render(request, 'faculty/findex.html', {})

def hindex(request):
    return render(request, 'hod/hindex.html', {})


# Checking semester views for list/grid view
def sem1(request):
    return render(request, 'faculty/sem1/sem1.html', {})
