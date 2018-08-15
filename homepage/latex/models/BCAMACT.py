from django.db import models

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
    update_count = models.PositiveIntegerField(default=0)

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
class SCAM(models.Model):
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

#Programming in Java
class PIJ(models.Model):
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

#Lab Java
class LJ(models.Model):
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

#Mobile Architecture and App Development
class MAAAD(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Server Operating System-I
class SOSI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Fundamentals of DataCenter
class FODC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Introduction to Cloud Technology
class ITCT(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Basic Android Programming
class BAP(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Introduction to Cloud Technology-Lab
class ITCTL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Basic Android Programming-Lab
class BAPL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Security Theats and Trends
class STAT(models.Model):
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

#Fundamentals of Storage
class FOS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Mobile Ecosystems and Business Models
class MEABM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Advanced Android Programming
class AAP(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Web Technology and Value Added Services in Mobile
class WTAVASIM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Principles of Virtualization
class POV(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Server Operating System-II
class SOSII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Server Operating System-II Lab
class SOSIIL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Advanced Android Programming-Lab
class AAPL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Security in Wireless, VoIP and Mobile Apps
class SIWVAMA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Android Security
class AS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# ------Subjects------
# --------------------
# ----BCA: Sem - 6----
# --------------------

#Mobile Testing
class MT(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

#Introduction to Windows Azure
class ITWA(models.Model):
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


