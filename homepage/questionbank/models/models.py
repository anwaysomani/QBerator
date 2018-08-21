from django.db import models

# Create your models here.

class UserProfile(models.Model):
    User = models.CharField(max_length=20)
    Extras = models.CharField(max_length=20)

