from django.urls import path
from django.conf.urls import url
from . import views
from .views import latex, faculty, hod

urlpatterns = [
        #url(r'^question/', views.question, name='question'),
        url(r'^$', views.latex.index, name='index'),
        url(r'form/$', views.latex.form, name='form'),
        url(r'list/$', views.latex.list, name='list'),
]
