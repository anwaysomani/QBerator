from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Main Structure page
    #url(r'^structure/$', views.StructureMain, name='structure'),

    # Base-pages
    url(r'^structure/$', views.indexPage, name='structure'),
   
   # Each ER Page
   url(r'individualER/$', views.individualER, name='individualER'),
]
