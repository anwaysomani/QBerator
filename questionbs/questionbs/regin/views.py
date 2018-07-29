from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from questionbs.regin.forms import SignUpForm

# Home Page(after_login)
@login_required
def home(request):
    return render(request, 'home.html')

# SignUp Form configuration
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# About Page(bef-af log)
def about(request):
    return render(request, 'subs/about.html')

# login form(using AJAX)
from django.views.generic import FormView
from .forms import JoinForm

class JoinFormView(FormView):
    form_class = JoinForm
    template_name = 'login.html'
    success_url = '/home'

    def form_invalid(self, form):
        response = super(JoinFormView, self). form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JoinFormView, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                    'message': "Succefully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response

# mixins addition
from .mixins import AjaxFormMixin

class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name = 'login.html'
    success_url = '/home'
