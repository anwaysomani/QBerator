from django.urls import path
from django.conf.urls import url
from . import views
from latex.views import facultyindex

urlpatterns = [
        url(r'^$', views.facultyindex, name='facultyindex'),

        # urls for faculty semester pages
        url(r'facsem1/$', views.facultysem1index, name='facsem1'),
        url(r'facsem2/$', views.facultysem2index, name='facsem2'),
        url(r'facsem3/$', views.facultysem3index, name='facsem3'),
        url(r'facsem4/$', views.facultysem4index, name='facsem4'),
        url(r'facsem5/$', views.facultysem5index, name='facsem5'),
        url(r'facsem6/$', views.facultysem6index, name='facsem6'),
        url(r'facsem7/$', views.facultysem7index, name='facsem7'),
        url(r'facsem8/$', views.facultysem8index, name='facsem8'),
]
