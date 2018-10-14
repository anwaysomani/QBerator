from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Testing custom user fields with AbstractUser

class Profile(models.Model):
    HOD = 1
    FACULTY = 2
    ROLE_CHOICES = (
            (1, 'Head-Of-Department'),
            (2, 'Faculty'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username

"""
class CustomUser(AbstractUser):
    HOD = 1
    FACULTY = 2
    ROLE_CHOICES = (
            (1, 'Head-Of-Department'),
            (2, 'Faculty'),
"""

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
