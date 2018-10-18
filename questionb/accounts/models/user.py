from django.contrib.auth import AbstractUser
from django.utils import timezone
from django.db import models


class User(AbstractUser):
    
    class Meta:
        permissions = (
                       ("can do something", "to say something"),
                       ("can do something 2", "to say something 2"),
                       ("can do something 3", "to say something 3"),
                      )

