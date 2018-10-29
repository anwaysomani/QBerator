from django.shortcuts import render, redirect

# Developer's page
def AboutDeveloper(request):
    return render(request, 'developerinfo.html', {})


