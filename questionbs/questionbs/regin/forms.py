from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    mobile_no = forms.IntegerField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'mobile_no', 'email', 'password1', 'password2', )

class JoinForm(forms.Form):
    employee_id = forms.IntegerField()
    password = forms.CharField()
