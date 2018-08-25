from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout


User = get_user_model()

class FacultyLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("This user does not exists")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(FacultyLoginForm, self).clean(*args, **kwargs)

class HODLoginForm(forms.Form):
    employee_id = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwarggs):
        employee_id = self.cleaned_data.get("employee_id")
        password = self.cleaned_data.get("password")

        if employee_id and password:
            user = authenticate(employee_id=employee_id, password=password)
            if not user: 
                raise forms.ValidationError("This user does not exists")
            if not user.chheck_password(password):
                raise forms.ValidationError("IncorrectPassword")

            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(HODLoginForm, self).clean(*args, **kwargs)
