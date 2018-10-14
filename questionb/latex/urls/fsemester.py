from django.conf.urls import include, url
from .. import views
from ..views import *

urlpatterns = [
    # urls for Faculty Semester views(extended)

    # Semester-1
    url(r'/fsem1/', views.sem1, name='fsem1'),
    # Semester-2
    url(r'/fsem2/', views.sem2, name='fsem2'),
    # Semester-3
    url(r'/fsem3/', views.sem3, name='fsem3'),
    # Semester-4
    url(r'/fsem4/', views.sem4, name='fsem4'),
    # Semester-5
    url(r'/fsem5/', views.sem5, name='fsem5'),
    # Semester-6
    url(r'/fsem6/', views.sem6, name='fsem6'),
    # Semester-7
    url(r'/fsem7/', views.sem7, name='fsem7'),
    # Semester-8
    url(r'/fsem8/', views.sem8, name='fsem8'),
]
