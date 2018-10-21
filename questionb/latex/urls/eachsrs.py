from django.conf.urls import include, url
from .. import views
from ..views import *

urlpatterns = [
        url(r'subject', views.quesdata_view, name='subject'),
]

