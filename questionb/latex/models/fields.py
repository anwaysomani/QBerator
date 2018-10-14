from django.db import models
from multiselectfield import MultiSelectField
from ..constant import *

# Model: Branch
class Branch1(models.Model):
    branch = models.CharField(max_length=75)
    br_abbr = models.CharField(max_length=10)

    def __str__(self):
        return self.branch

# Model: Specialization
class Specialization1(models.Model):
    branch = models.ForeignKey(Branch1)
    specialization1 = models.CharField(max_length=30)
    sp1_abbr = models.CharField(max_length=5)
    specialization2 = models.CharField(max_length=30, null=True)
    sp2_abbr = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.sp1_abbr + "" + self.sp2_abbr  

# Model: Semester
class Semester1(models.Model):
    branch = models.ForeignKey(Branch1)
    semesters = MultiSelectField(choices=SEM_CHOICES)

    def __str__(self):
        return "Text2"
    
# Model: Subject
class Subject1(models.Model):
    branch = models.ForeignKey(Branch1)
    semester = models.ForeignKey(Semester1)
    subject = models.CharField(max_length=75)

    def __str__(self):
        return self.subject

# Model: Module
class Module1(models.Model): 
    subject = models.ForeignKey(Subject1)
    module = models.CharField(max_length=75)

    def __str__(self):
        return self.module

# Model: Chapter
class Chapter1(models.Model):
    subject = models.ForeignKey(Module1)
    chapter = models.CharField(max_length=150)
    
    def __str__(self):
        return self.chapter

