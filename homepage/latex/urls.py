from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^CreateQues/$', views.CreateQues, name='CreateQues'),
]   
