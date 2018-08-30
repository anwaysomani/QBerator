from django.conf.urls import include, url
from .. import views

urlpatterns = [
    # Post Login Urls

    # Post HOD Login
    url(r'hindex/$', views.hindex, name='hindex'),

    # Post Faculty Login
    url(r'findex/$', views.findex, name='findex'),
]
