from django.db import models
from django.contrib.auth.models import User

# Login form
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    employee_id = models.IntegerField()

    def __unicode__(self):
        return self.user.username

