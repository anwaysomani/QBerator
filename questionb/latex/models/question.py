from django.db import models
from ..constant import *
from multiselectfield import MultiSelectField

from .fields import Subject

# Fields: 
class Question(models.Model):
    #subject_code = models.CharField(max_length=6, blank=True)
    block = models.IntegerField()
    subject_id = models.IntegerField(null=True, blank=True)
    modules = models.CharField(max_length=100, choices=MOD_CHOICES)
    question = models.CharField(max_length=300)
    marks = models.IntegerField(choices=MARKS_CHOICES, null=True)
    priority = models.IntegerField(choices=PRI_CHOICES)
    notes = models.CharField(max_length=300)

    def __str__(self):
        return self.question
