from django.conf.urls import include, url
from .. import views
from ..views import *

urlpatterns = [
        #url(r'subject/', views.quesdata_view, name='subject'),
        url(r'subject/(?P<id>\d+)', views.quesdata_view, name='eachsubject'),

        # (?P<id>\d+)

        # ------------------------------------------------------------------
        # Trial pattern for exporting to pdf
        url(r'epdf/', views.html_to_pdf_view, name='epdf'),
]

