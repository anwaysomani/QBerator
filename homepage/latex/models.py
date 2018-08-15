from django.db import models

class Test(models.Model):
    test_one = models.CharField(max_length=20)
    test_two = models.CharField(max_length=20)
