from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    contact_no = models.BigIntegerField()
    profile_pic = models.ImageField()
    employee_id = models.CharField(max_length=8)
    join_date = models.DateField()

