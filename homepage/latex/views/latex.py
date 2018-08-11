from django.shortcuts import render
from ..forms import InsQuestion 
from django.urls import reverse

#Views for trial editing
"""from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.resolvers import reverse_lazy
from latex.models import InsQuestion"""

# view '2' for creating Index Page
"""class IndexView(generic.ListView):
    # list of objects on Index page
    context_object_name = 'question_list'
    template_name = 'base.html'

    def get_queryset(self):
        return InsQuestion.objects.all()"""


# view for displaying 'just' HTML document
def index(request):
    return render(request, 'base.html')

# view for displaying 'just' HTML document
def form(request):
    if request.method == "POST":
        form = InsQuestion(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InsQuestion()

        return render(request, 'registration/form.html', {'form': form})

# view for displayin list.html
def list(request):
    return render(request, 'list.html')

# view trial'ed' for completion page of django
def done(request):
    return render(request, 'done.html')

# SignUpView
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'
