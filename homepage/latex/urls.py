from django.conf.urls import url
from . import views
from latex.views import facultyindex
from latex.views import English_I_CreateView, English_I_ListView, CFAO_CreateView, CFAO_ListView

# For Login System
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
        # Login System (fac)
        url(r'^login/$', auth_views.login, name='login'),
        url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
        url(r'^admin/', admin.site.urls),
    
        # Index(random)
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
        # English-I
        url(r'^EnglishIC/$', English_I_CreateView.as_view(), name="english_I"),
        url(r'EnglishIL/$', English_I_ListView.as_view(), name="english_i_list"),
        # CFAO
        url(r'^CFAOC/$', CFAO_CreateView.as_view(), name="cfao"),
        url(r'CFAOL/$', CFAO_ListView.as_view(), name="cfao_list"),

]
