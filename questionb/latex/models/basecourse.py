from django.db import models

# Consist: Branch, Specialization, Semester
class BranchSem(models.Model):
    branch = models.CharField(max_length=50)
    specialization = models.CharField(max_length=70)
    abbrevation = models.CharField(max_length=20)
    SEM_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    ]
    semester = models.IntegerField(choices=SEM_CHOICES)
    
    def __str__(self):
        return self.abbrevation


# Consist: Subject, Subject Code, Module Type
class Subject(models.Model):
    branch = models.ForeignKey(BranchSem)
    #specialization = models.ForeignKey(BranchSem)
    subject = models.CharField(max_length=70, unique=True)
    sub_code = models.CharField(max_length=6, unique=True, primary_key=True)
    module_type = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.subject
        
