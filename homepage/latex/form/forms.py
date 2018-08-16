from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

class UserRegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
