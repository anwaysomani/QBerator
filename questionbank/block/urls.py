from django.conf.urls import url, include

urlpatterns = [
        url('^accounts/', include('django.contrib.auth.urls')),
]
