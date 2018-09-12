from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)

            return redirect('findex/')
        
        
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
