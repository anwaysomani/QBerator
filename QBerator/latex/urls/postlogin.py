"""
Urls for post-login pages

Developer: Anway Somani

"""


from django.conf.urls import include, url
from .. import views

urlpatterns = [
    # Post HOD Login
    url(r'hindex', views.hindex, name='hindex'),

    # Post Faculty Login
    url(r'findex', views.findex, name='findex'),

    # Trial check for errors
    url(r'error', views.error, name='error'),
]
