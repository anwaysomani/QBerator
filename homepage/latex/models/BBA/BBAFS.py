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
# ----BBA: Sem - 1----
# --------------------

# Principles of Management
class POM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Business Accounting
class BA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Business Statistics
class BS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Business Law
class BL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Personality Development
class PD(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# French-I
class FI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Excel Applications for Business
class EAFB(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# ------Subjects------
# --------------------
# ----BBA: Sem - 2----
# --------------------

# Marketing Management
class MM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Business Mathematics
class BM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Research Methodology
class RM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Basics of Cost Accounting
class BOCA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# French-II
class FII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Business Communication-I
class BCI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Health Education and Fitness
class HEAF(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# ------Subjects------
# --------------------
# ----BBA: Sem - 3----
# --------------------

# Business Environment
class BE(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Managerial Economics
class ME(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Financial Management
class FM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Human Resource Management
class HRM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Business Communication-II
class BCII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Time & Stress Management
class TASM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Environmental Studies
class ES(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# ------Subjects------
# --------------------
# ----BBA: Sem - 4----
# --------------------

# Indian Financial System
class IFS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Industrial Laws
class IL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Management Accounting
class MA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Summer Project
class SP(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Financial Planning
class FP(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Advanced Quantitative Techniques
class AQT(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Financial Services
class FS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# ------Subjects------
# --------------------
# ----BBA: Sem - 5----
# --------------------

# Business Information System
class BIS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Consumer Relationship Management
class CRM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Insuarance and Risk Management
class IARM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# International Finance
class IF(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Derivatives and Commodities Market
class DACM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Strategic Management
class SM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Business Planning & Project Management
class BPAPM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# ------Subjects------
# --------------------
# ----BBA: Sem - 6----
# --------------------

# Production & Material Management
class PAMM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Project Study
class PS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Taxation
class T(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Financial Modelling Using Excel
class FMUE(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Security Analysis & Portfolio Management
class SAAPM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

