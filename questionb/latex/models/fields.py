from django.db import models
from multiselectfield import MultiSelectField
from ..constant import *

from django.core.validators import MaxValueValidator, MinValueValidator

# Model: Branch
class Branch(models.Model):
    branch = models.CharField(max_length=75)
    br_abbr = models.CharField(max_length=20)

    def __str__(self):
        return self.branch

# Model: myDeclareSemesterModel
#class DeclareSemester(models.Model):
#    semester = models.CharField(max_length=6)

#    def __str__(self):
#        return self.semester

# Model: Specialization
class Specialization(models.Model):
    branch = models.ForeignKey(Branch)
    specialization1 = models.CharField(max_length=30)
    specialization2 = models.CharField(max_length=30, blank=True)
    abbreviation = models.CharField(max_length=20)
#   semester = models.ForeignKey(DeclareSemester, null=True)

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
    subject = models.CharField(max_length=75)
    subject_code = models.CharField(max_length=6, null=True)
    module_type = models.CharField(max_length=2, null=True)
    credits = models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)], null=True)

    #class Meta:
    #    unique_together = [("specialization", "subject")]
    
    def clean_module_type(self):
        return self.cleaned_data["module_type"].upper()

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

