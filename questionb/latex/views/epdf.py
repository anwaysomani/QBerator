from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from ..models import Subject, Question

from weasyprint import HTML

def html_to_pdf_view(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    user = request.user
    lister = user.profile.subject.all()
    query = Question.objects.all()

    html_string = render_to_string('pdf/pdf_template.html', {'paragraphs': lister, 'user': user, 'query': query})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response
