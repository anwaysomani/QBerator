from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Developer Information
    url(r'^aboutdeveloper/$', views.AboutDeveloper, name='about_developer'),
]
