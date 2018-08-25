from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_faculty = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)

class Faculty(models.Model):
    username = models.CharField(max_length=`
