from django.db import models
from ..constant import *
from multiselectfield import MultiSelectField

# Fields: 
class AQuestion(models.Model):
    modules = models.CharField(max_length=100, choices=MOD_CHOICES)
    question = models.CharField(max_length=300)
    marks = MultiSelectField(choices=MARKS_CHOICES)
    priority = MultiSelectField(choices=PRI_CHOICES)
    notes = models.CharField(max_length=300)

    def __str__(self):
        return self.question
    
