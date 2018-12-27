"""
Models declarations for accounts: User-Models
"""

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from latex.models import *

# Permission fields for subject in user registration (admininstrator)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.user.username

# -----------------------------------------------------------------------------

# Sfl contri: for middlewares
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
# -----------------------------------------------------------------------------

