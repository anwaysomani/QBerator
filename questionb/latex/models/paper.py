from django.db import models
from .fields import Subject

class QuestionPaper(models.Model):
    Subject = models.ForeignKey(Subject)
    QuestionPaper = models.FileField()
