"""
Models for admin field. Accesible to adminsitrator. By law_er_rule
Models engaged: Branch, Specialization, Semester, Subject, Module, Chapter

Developer: Anway Somani

"""

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Model: Branch
class Branch(models.Model):
    branch = models.CharField(max_length=75)
    br_abbr = models.CharField(max_length=20)

    def __str__(self):
        return self.branch

# Model: Specialization
class Specialization(models.Model):
    branch = models.ForeignKey(Branch)
    specialization1 = models.CharField(max_length=30)
    specialization2 = models.CharField(max_length=30, blank=True)
    abbreviation = models.CharField(max_length=20)

    def __str__(self):
        return self.branch.br_abbr + " " + self.abbreviation

# Mdoel: Semester
class Semester(models.Model):
    specialization = models.ForeignKey(Specialization)
    semester = models.CharField(max_length=7)

    class Meta:
        unique_together = [("specialization", "semester")]

    def __str__(self):
        return self.specialization.branch.br_abbr + " " + self.specialization.abbreviation + " " + self.semester
    

# Model: Subject
class Subject(models.Model):
    semester = models.ManyToManyField(Semester)
    subject = models.CharField(max_length=75, unique=True)
    subject_code = models.CharField(max_length=6, null=True, blank=True)
    module_type = models.CharField(max_length=2, null=True, blank=True)
    credits = models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)], null=True, blank=True)

    def clean_module_type(self):
        return self.cleaned_data["module_type"].upper()

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.subject

# Model: Module
class Module(models.Model): 
    subject = models.ForeignKey(Subject)
    module = models.CharField(max_length=75)

    def __str__(self):
        return self.module

# Model: Chapter
class Chapter(models.Model):
    subject = models.ForeignKey(Module)
    chapter = models.CharField(max_length=150)
    
    def __str__(self):
        return self.chapter

