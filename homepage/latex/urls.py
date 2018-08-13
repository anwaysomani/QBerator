from django.urls import path
from django.conf.urls import url
from . import views
from latex.views import facultyindex

urlpatterns = [

        # index after Faculty Login
        url(r'faculty/^$', views.facultyindex, name='facultyindex'),

        # urls for faculty semester pages
        url(r'faculty/facsem1/$', views.facultysem1index, name='facsem1'),
        url(r'faculty/facsem2/$', views.facultysem2index, name='facsem2'),
        url(r'faculty/facsem3/$', views.facultysem3index, name='facsem3'),
        url(r'faculty/facsem4/$', views.facultysem4index, name='facsem4'),
        url(r'faculty/facsem5/$', views.facultysem5index, name='facsem5'),
        url(r'faculty/facsem6/$', views.facultysem6index, name='facsem6'),
        url(r'faculty/facsem7/$', views.facultysem7index, name='facsem7'),
        url(r'faculty/facsem8/$', views.facultysem8index, name='facsem8'),
]
