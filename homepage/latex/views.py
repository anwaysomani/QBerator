from django.shortcuts import render







# index page of faculty containing view option and all accordions
def facultyindex(request):
    return render(request, 'index/faculty_index.html', {})

def facultysem1index(request):
    return render(request, 'faculty/index/index_sem1.html', {})

def facultysem2index(request):
    return render(request, 'faculty/index/index_sem2.html', {})

def facultysem3index(request):
    return render(request, 'faculty/index/index_sem3.html', {})

def facultysem4index(request):
    return render(request, 'faculty/index/index_sem4.html', {})

def facultysem5index(request):
    return render(request, 'faculty/index/index_sem5.html', {})

def facultysem6index(request):
    return render(request, 'faculty/index/index_sem6.html', {})

def facultysem7index(request):
    return render(request, 'faculty/index/index_sem7.html', {})

def facultysem8index(request):
    return render(request, 'faculty/index/index_sem8.html', {})
