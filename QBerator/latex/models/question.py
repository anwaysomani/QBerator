"""
Model for question, link to db
app: latex

"""

from django.db import models
from ..constant import MOD_CHOICES, MARKS_CHOICES, PRI_CHOICES
#from .fields import Subject

#CKEditor
from ckeditor_uploader.fields import RichTextUploadingField

# Model: Question
class Question(models.Model):
    block    = models.IntegerField()
    modules  = models.CharField(max_length=100, choices=MOD_CHOICES)
    question = RichTextUploadingField()
    marks    = models.IntegerField(choices=MARKS_CHOICES, null=True)
    priority = models.IntegerField(choices=PRI_CHOICES)
    notes    = models.TextField(null=True)

    def __str__(self):
        return self.question

class SubjectCategory(models.Model):
    total_marks   = models.CharField(max_length=4, primary_key=True)
    required_2mk  = models.IntegerField(null=True)
    maximum_2mk   = models.IntegerField(null=True)
    required_5mk  = models.IntegerField(null=True)
    maximum_5mk   = models.IntegerField(null=True)
    required_10mk = models.IntegerField(null=True)
    maximum_10mk  = models.IntegerField(null=True)

    def __str__(self):
        return self.total_marks

    class Meta:
        verbose_name = ('Subject Category')
        verbose_name_plural = ('Subject Categories')


