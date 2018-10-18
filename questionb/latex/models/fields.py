from django.db import models
from multiselectfield import MultiSelectField
from ..constant import *

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

# Model: myDeclareSemesterModel
class DeclareSemester(models.Model):
    semesters = models.CharField(max_length=6)

    def __str__(self):
        return self.semesters


# Model: Semester
class Semester(models.Model):
    branch = models.ForeignKey(Branch)
    semesters = models.ForeignKey(DeclareSemester, default='Sem-')

    def __str__(self):
        return self.branch.branch + "-  " + self.semester.semester

# Model: Subject
class Subject(models.Model):
    branch = models.ForeignKey(Branch)
    semester = models.ForeignKey(Semester)
    subject = models.CharField(max_length=75)

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

