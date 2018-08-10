from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import QuestionBlockForm

class HomeView(TemplateView):
    template_name = 'home.html'

def about(request):
    return render(request, 'subs/about.html')

def CreateQues(request):
    return render(request, 'Questionnaire/create.html', {})

def showform(request):
    form = QuestionBlockForm()
    
    if request.POST:
        if form.is_valid():
            QuestionBlock = form.save()
        return redirect('/base/')

    return render_to_response('Questionnnaire/create.html',{
        'form': form
    },context_instance=RequestContext(request))


