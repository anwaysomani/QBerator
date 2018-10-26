"""
Url configuration for Authentication pages
- Login Page(F&H)
- Redirection post-login(default)

Developer: Anway Somani

"""


from django.conf.urls import include, url
from . import views
from .views import PanelRedirectView, login, logout
from django.views.generic.base import RedirectView

urlpatterns = [
    # login
    url(r'^accounts/login/', views.login, name='login'),

    # Panel Redirection for authenticated users(hidden due to respect!)
    url(r'^panel-redirect/$', PanelRedirectView.as_view(), name='panel-redirect'),

    # Password change
    url(r'^password/$', views.change_password, name='change_password'),

    # ----------------------------------------------------------------------------
    # Developer Options
    url(r'^aboutdeveloper/$', views.AboutDeveloper, name='about_developer'),
]
