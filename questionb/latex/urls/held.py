from django.conf.urls import include, url
from .. import views
from ..views import *

urlpatterns = [
    url(r'main/$', views.main, name='main'),

    # Faculty Login
    url(r'^flogin/', views.faculty_login, name='faculty-login'),

    # HOD Login
    url(r'^hlogin/', views.hod_login, name='hod-login'),

]
