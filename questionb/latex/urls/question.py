from django.conf.urls import include, url
from .. import views

urlpatterns = [
    url(r'findex/fsem1/ratii/$', views.RATII, name='ratii'),
]
