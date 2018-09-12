from django.conf.urls import include, url
from .. import views

urlpatterns = [
    # For Login
    url(r'^login/$', views.login_view, name='login'),

    # For Signup
    # url(r'^signup/$', views.signup_view, name='signup'),
]
