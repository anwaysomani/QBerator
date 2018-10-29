from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from ..models import Subject, Question

from weasyprint import HTML

def html_to_pdf_view(request, id):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    user = request.user
    query = Question.objects.filter(block=id)

    html_string = render_to_string('pdf/pdf_template.html', {'user': user, 'query': query, 'id': id})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response

def generate_pdf(request, subject_id):
    user = request.user
    subjects = Subject.objects.filter(id=subject_id)
    questions = Question.objects.filter(block=subject_id)

    # First Case: 50 marks
    fifties_twomarks = Question.objects.filter(block=subject_id, marks=2).order_by('?')[:5]
    fifties_fivemarks = Question.objects.filter(block=subject_id, marks=5).order_by('?')[:4]
    fifties_tenmarks = Question.objects.filter(block=subject_id, marks=10).order_by('?')[:2]

    # Second Case: 30 marks
    thirties_twomarks = Question.objects.filter(block=subject_id, marks=2).order_by('?')[:5]
    thirties_fivemarks = Question.objects.filter(block=subject_id, marks=5).order_by('?')[:2]
    thirties_tenmarks = Question.objects.filter(block=subject_id, marks=10).order_by('?')[:1]

    # Third Case: 20 marks
    twenties_twomarks = Question.objects.filter(block=subject_id, marks=2).order_by('?')[:5]
    twenties_fivemarks = Question.objects.filter(block=subject_id, marks=5).order_by('?')[:2]
    twenties_tenmarks = Question.objects.filter(block=subject_id, marks=10).order_by('?')[:1]


    context = {
               'subjects': subjects,
               'questions': questions,
               
               # First Case
               'fifties_twomarks': fifties_twomarks,
               'fifties_fivemarks': fifties_fivemarks,
               'fifties_tenmarks': fifties_tenmarks,
               # Second Case
               'thirties_twomarks': thirties_twomarks,
               'thirties_fivemarks': thirties_fivemarks,
               'thirties_tenmarks': thirties_tenmarks,
               # Third Case
               'twenties_twomarks': twenties_twomarks,
               'twenties_fivemarks': twenties_fivemarks,
               'twenties_tenmarks': twenties_tenmarks,
    }

    print("Arriving here....")
    html_string = render_to_string('pdf/pdf_template.html', context)

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/questionpaper.pdf');
   
    fs = FileSystemStorage('/tmp')
    with fs.open('questionpaper.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="questionpaper.pdf"'
        return response

    return response

    if subjects.module_type is 30:
        print("Balle")
    elif subjects.category is 20:
        print("Bada balle")
    elif subjects.category is 50:
        print("Sabse bada balle")
    else:
        print("Checking balle's")



