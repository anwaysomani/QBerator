"""questionb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# Django built-in login
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Urls from admin
    url(r'^admin/', admin.site.urls),

    # Urls from latex
    
    # includes urls for login(Ajeenkya DY Patil University: seperated login for Faculty and HoD
    url('', include('latex.urls.login')),
   
    # Post Login to: 'findex', 'hindex'
    url('', include('latex.urls.postlogin')),
    
    # finde to fsem1-fsem8 
    url('', include('latex.urls.fsemester')),

]
