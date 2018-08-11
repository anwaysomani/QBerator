from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        #url(r'^question/', views.question, name='question'),
        #url(r'^$', views.latex.index, name='index'),
        #url(r'form/$', views.latex.form, name='form'),
        #url(r'list/$', views.latex.list, name='list'),
        url(r'^$', views.index, name='index'),
        url(r'createquestion/$', views.CreateQuest, name='createquestion'),
]
