"""
Model for question, link to db
app: latex

Developer: Anway Somani

"""

from django.db import models
from ..constant import MOD_CHOICES, MARKS_CHOICES, PRI_CHOICES
from .fields import Subject

# Model: Question
class Question(models.Model):
    block = models.IntegerField()
    modules = models.CharField(max_length=100, choices=MOD_CHOICES)
    question = models.TextField(unique=True)
    marks = models.IntegerField(choices=MARKS_CHOICES, null=True)
    priority = models.IntegerField(choices=PRI_CHOICES)
    notes = models.TextField()

    def __str__(self):
        return self.question

class QuestionCategory(models.Model):
    total_marks = models.IntegerField()
    req_2mk     = models.IntegerField()
    max_2mk     = models.IntegerField()
    req_5mk     = models.IntegerField()
    max_5mk     = models.IntegerField()
    req_10mk    = models.IntegerField()
    max_10mk    = models.IntegerField()

    def __str__(self):
        return self.total_marks
