"""
Urls for CRUD operations

Developer: Anway Somani

"""
from django.conf.urls import include, url
from .. import views
from ..views import quesdata_view, QuestionUpdate, QuestionDelete

urlpatterns = [
        url(r'subject/(?P<id>\d+)', views.quesdata_view, name='eachsubject'),

        # ------------------------------------------------------------------
        # Trial pattern for exporting to pdf
        url(r'epdf/', views.html_to_pdf_view, name='epdf'),

        # ------------------------------------------------------------------
        # Generic views
        # Update
        url(r'question/(?P<pk>\d+)/update/', views.QuestionUpdate.as_view(), name='question-update'),
        # Delete
        url(r'question/(?P<pk>\d+)/delete/$', views.QuestionDelete.as_view(), name='question-delete'),
]

