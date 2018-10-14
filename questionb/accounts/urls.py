from django.conf.urls import include, url
from . import views
from .views import *
from .views import PanelRedirectView
from django.views.generic.base import RedirectView
#from .views import PanelRedirectView

urlpatterns = [
    # seperated login view for faculty and hod with base
    #url(r'^main/$', views.main, name='main'),

    # Faculty Login
    #url(r'flogin/', views.faculty_login, name='faculty-login'),

    # HOD Login
    #url(r'hlogin/', views.hod_login, name='hod-login'),

    # login
    url(r'^accounts/login/', views.login, name='login'),

    # redirect view trial
    url(r'^panel-redirect/$', PanelRedirectView.as_view(), name='panel-redirect'),

]
