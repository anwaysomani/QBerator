from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic.base import RedirectView

# # Views below: v

def login(request):
        title = "Login Form"

        return render(request, "registration/login.html", {"title": title})

# Creating new redirect view
class PanelRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.groups.filter(name='HOD').count():
            return redirect('/hindex/$')
        elif user.groups.filter(name='Faculty').count():
            return redirect('findex/$')
        else:
            return redirect('error/$')

