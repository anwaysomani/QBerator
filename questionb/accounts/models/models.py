from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from multiselectfield import MultiSelectField

from latex.models import *

# Importing constants
from ..constants import *

# Testing custom user fields with AbstractUser

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #subject = models.CharField(max_length=20, null=True, choices=SUBJECT)
    subject = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



