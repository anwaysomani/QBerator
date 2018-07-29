import datetime
import uuid

from django.contrib.auth import User
from django.db import models
from django.urls import reverse


def get_file_name(file_name):
    '''
    This will return a randomly generated file name
    of 16 characters

    Note -
    ----
    Extension does not persist.

    '''

    file_name = str(uuid.uuid4())
    return file_name
    

class UserProfile(User):
    middle_name = models.CharField(max_length=30)
    contact_number = models.BigIntegerField()
    employee_id = models.CharField(max_length=16)
    date_of_joining = models.DateField()
    gender = models.CharField()
    profile_picture = models.ImageField(upload_to=get_file_name())

