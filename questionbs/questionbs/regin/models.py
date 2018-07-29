import datetime
import uuid

from django.contrib.auth.models import User
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
    

class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    contact_number = models.BigIntegerField()
    employee_id = models.CharField(max_length=16)
    date_of_joining = models.DateField()
    gender = models.CharField(max_length=7)
    profile_picture = models.ImageField(upload_to=get_file_name)
    is_faculty = models.BooleanField(default=True)
    is_hod = models.BooleanField(default=False)
    departmenet = models.CharField(max_length=30)

class Question(models.Model):
    description = models.TextField(max_length=250)
    title = models.CharField(max_length=30)
    tag = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50)
    answer = models.TextField(max_length=250)
    max_marks = models.FloatField()
    category = models.CharField(max_length=50)
    branch = models.CharField(max_length=40)
    course = models.CharField(max_length=35)
    subject = models.CharField(max_length=30)
    module = models.CharField(max_length=30)
    chapter = models.CharField(max_length=30)
    state = models.CharField(max_length=100)
    created_by = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    used_count = models.IntegerField()

