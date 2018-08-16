from django.conf.urls import url
from . import views
from latex.views import facultyindex
from latex.views import English_I_CreateView, English_I_ListView

urlpatterns = [

        url(r'index/$', views.index, name='index'),

        # index after Faculty Login
        url(r'faculty/$', views.facultyindex, name='facultyindex'),

        # urls for faculty semester pages
        url(r'faculty/facsem1/$', views.facultysem1index, name='facsem1'),
        url(r'faculty/facsem2/$', views.facultysem2index, name='facsem2'),
        url(r'faculty/facsem3/$', views.facultysem3index, name='facsem3'),
        url(r'faculty/facsem4/$', views.facultysem4index, name='facsem4'),
        url(r'faculty/facsem5/$', views.facultysem5index, name='facsem5'),
        url(r'faculty/facsem6/$', views.facultysem6index, name='facsem6'),
        url(r'faculty/facsem7/$', views.facultysem7index, name='facsem7'),
        url(r'faculty/facsem8/$', views.facultysem8index, name='facsem8'),

        # django modals for BCA-MACT
        url(r'^EnglishIC/$', English_I_CreateView.as_view(), name="english_I"),
        url(r'EnglishIL/$', English_I_ListView.as_view(), name="english_i_list"),
]
