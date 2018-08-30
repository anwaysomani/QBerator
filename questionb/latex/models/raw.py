from django.db import models
from multiselectfield import MultiSelectField
from ..constant import *

# Models: branch, specialization, semester, br_abbreviation
class Branch(models.Model):
    branch = models.CharField(max_length=70)
    specialization = MultiSelectField(choices=SPEC_CHOICES)
    br_abbreviation = models.CharField(max_length=15)

    def __str__(self):
        return self.br_abbreviation

# Models: branch(foreign), semester, sem_abbreviation, course(foreign)
class Semester(models.Model):
    branch = models.ForeignKey(Branch)
    semester = models.IntegerField(choices=SEM_CHOICES)
    sem_abbreviation = models.CharField(max_length=15)
    
    def __str__(self):
        return self.sem_abbreviation


# Models: semester(foreign), course, course_code, credit, module_type
class Course(models.Model):
    semester = models.ForeignKey(Semester)
    course = models.CharField(max_length=70)
    course_code = models.CharField(max_length=6)
    credit = models.IntegerField(choices=CREDIT_CHOICES)
    module_type = models.CharField(max_length=2, choices=MODULE_TYPE_CHOICES)
    
    def __str__(self):
        return self.course

# Models: course(foreign), module
class Modules(models.Model):
    sem_abbreviation = models.ForeignKey(Course)
    module = models.CharField(max_length=70)

    def __str__(self):
        return self.module



# Declaring Itemss:
"""
    For multi-line coding, this is enabled.
    But, to the most different ways, there cannot be any modal for a form.
    """
