"""
For Middleware including SingleSessionUser
Developer:Anway Somani
"""

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

user = settings.AUTH_USER_MODEL

# Model to store the list of logged_in user
class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user')
    # Session Keys(32-character long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username

