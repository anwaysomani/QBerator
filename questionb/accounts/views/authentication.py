"""
User Certification for granted access to post-login urls

Developer: Anway Somani

"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic.base import RedirectView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Views for Authentication based-working
# --------------------------------------

# LogIn
def login(request):
        return render(request, "registration/login.html", {"title": title})

# LogOut
def logout_view(request):
    logout(request)

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# Creating new redirect view
class PanelRedirectView(RedirectView):

    # Checking user group for redirecting based on user-role
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.groups.filter(name='HOD').count():
            return redirect('/hindex/$')
        elif user.groups.filter(name='Faculty').count():
            return redirect('findex/$')
        else:
            return redirect('error/$')


# Password change View
# --------------------
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/pwdchange.html', {
        'form': form
    })

