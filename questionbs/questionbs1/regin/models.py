from django.db import models
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('regin:index')
