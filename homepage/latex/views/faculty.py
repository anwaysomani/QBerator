from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from ..decorators import faculty_required
from ..models import Question

@login_required
@faculty_required
def InsQuestion(request, pk):
    question = get_object_or_404(Question, pk=pk)
    faculty = request.user.faculty

    return render(request, 'registration/form.html', {
        'question': question,
        'form': form,
        'progress': progress
    })

#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required
#from ..decorators import faculty_required

from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import FacultySignUpForm
from ..models import User

class FacultySignUpView(CreateView):
    model = User
    form_class = FacultySignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type']='faculty'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = forms.save()
        login(self.request, user)
        return redirect('faculty:form')
