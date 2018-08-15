form django.db import models

# Common Choices
# --------------
# Common Modules
MOD_CHOICES = (
        ('M1', 'M1'),
        ('M2', 'M2'),
        ('M3', 'M3'),
        ('M4', 'M4'),
        ('M5', 'M5'),
)

# Common Marks
MARKS_CHOICES = (
        ('2', '2'),
        ('5', '5'),
        ('10', '10'),
)

# Common Priority
PRIORITY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
)


# ------Subjects------
# --------------------
# ----BCA: Sem - 1----
# --------------------

#English - I
class EI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Fundamentals Of Mathematics
class FOM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Effective Speaking and Analytical Skills-I
class ESASI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Computer Fundamentals & Organizations
class CFAO(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Introduction to Linux
class ITL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Programming in C
class PIC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#C Programming Lab
class CPL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Linux Lab
class LL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# ------Subjects------
# --------------------
# ----BCA: Sem - 2----
# --------------------

#English-II
class EII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Effective Speaking and Analytical Skills-II
class ESASII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Reasoning and Thinking-I
class RATI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Operating System
class OS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Data Structures Using C
class DSUC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#OOPs with C++
class OWCPP(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#System Configuration and Maintenance
class SCM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Data Structure Lab
class DSL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#C++ Lab
class CPPL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# ------Subjects------
# --------------------
# ----BCA: Sem - 3----
# --------------------

#Reasoning and Thinking-II
class RATII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Employability Skills
class ES(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Computer Networks
class CN(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Software Engineering
class SE(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Information Security Fundamentals
class ISF(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Introduction to Web Technology
class ITWT(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Introduction to DBMS
class ITD(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Introduction to Web Technology Lab
class ITWTL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Lab DBMS
class LD(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# ------Subjects------
# --------------------
# ----BCA: Sem - 4----
# --------------------

#Environmental Studies
class ES(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Introduction to UI/UX
class ITUU(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Object Oriented Analysis and Design
class OOAAD(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Interactive Web Application Development
class IWAD(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Programming in Java
class PIJ(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Principles of Programming Languages
class POPL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Lab Java
class LJ(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Interactive Web Application Development-Lab
class IWADL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Probablity and Statistics
class PAS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Computer Oriented Numerical Methods
class CONM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# ------Subjects------
# --------------------
# ----BCA: Sem - 5----
# --------------------

#Professional Skills
class PS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Enterprise Application Development
class EAD(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Distributed Systems
class DS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#JavaScript Frameworks
class JSF(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Server-side Scripting
class SSS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Data Communication
class DC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Computer Graphics
class CG(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Server-side Scripting-Lab
class SSSL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Enterprise Application Development-Lab
class EADL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#E-Commerce
class EC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Disaster Recovery and Business Continuity Management
class DRABCM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# ------Subjects------
# --------------------
# ----BCA: Sem - 6----
# --------------------

#Entrepreneurship Development
class ED(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#ITIL
class ITIL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Major Project/Internship
class MPI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

