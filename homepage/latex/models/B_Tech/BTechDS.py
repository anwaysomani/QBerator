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
# --B. Tech: Sem - 1--
# --------------------

# Linear Algebra & Differential Calculus
class LAADC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Know Your Science
class KYS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Enhancement of Communication Skills
class EOCS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Engineering Design-I
class EDI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Introduction to Computing Environment
class ITCE(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Bridge Courses in Mathematics
class BCIM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# --B. Tech: Sem - 2--
# --------------------

# Differential Equations and Integral Calculus
class DEAIC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Mechanics
class M(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Engineering Professionalism and Ethics
class EPAE(models.Model):
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

# Computer Aided Engineering Graphics
class CAEG(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Engineering Design-II
class EDII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Bridge Course on Electronics
class BCOE(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# --B. Tech: Sem - 3--
# --------------------

# Statistics and Probablity - I
class SAPI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Economics for Engineers
class EFE(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Data Structures
class DS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Object Oriented Programming Using Java
class OOPUJ(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Relational Database Management System
class RDBMS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Analysis & Design of Algortihms
class AADOA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Introduction to Communication Skills
class ITCS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# --B. Tech: Sem - 4--
# --------------------

# Operating System
class OS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Statistics and Probablity - II
class SAPII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Database Visualization
class DV(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Data Analytics Using SQL
class DAUS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Information Security Fundamentals
class ISF(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# NoSQL Databases
class ND(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Scientific Programming Using R
class SPUR(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# --B. Tech: Sem - 5--
# --------------------

# Inferential Statistics
class IS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Advance Data Analysis Using SQL
class ADAUS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Big Data Analysis - I
class BDAI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Machine Learning Algorithms - I
class MLAI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Reasoning and Thinking
class RAT(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Optimization Techniques
class OT(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Free Elective - I
class FEI(models.Model):
    modules = models.CharField(chooices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Employability Skills
class ES(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# --B. Tech: Sem - 6--
# --------------------

# Python Programming for Data Scientist
class PPFDS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Data Analytics Using MS Excel
class DAUME(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Exploratory Data Analysis 
class EDA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Big Data Analysis - II
class BDAII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Cloud Computing
class CC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Mobile Computing
class MC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Internet of Things
class IOT(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Natural Language Processing
class NLP(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Neural Networks
class NN(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Recommender System
class RS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Free Elective-II
class FEII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Professional Skills
class PS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# --B. Tech: Sem - 7--
# --------------------

# Machine Learning Algortihms - II
class MLAII(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Artificial Intellignece
class AI(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Time Series Analysis
class TSA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Dimensionality Reduction and Model Validation
class DRAMV(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Deep Learning
class DL(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Advance Optimization Techniques
class AOT(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Big Data Analyics on Cloud
class BDAOC(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Advance Machine Learning Algortihms
class AMLA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Artificial Intelligence Algorithms
class AIA(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Advance Data Visualization
class ADV(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Data Science Project Management
class DSPM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Software Engineering
class SE(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Agile Methodology
class AM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)


# --B. Tech: Sem - 8--
# --------------------

# Latest Trends in Data Science
class LTIDS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Advance Statistical Modelling
class ASM(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Real Time Data Processing
class RTDP(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Business Communication and Presentation Skills
class BCAPS(models.Model):
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

# Major Project/Internship
class MPI(models.Model):i
    modules = models.CharField(choices=MOD_CHOICES, max_length=60)
    question = models.CharField(max_length=500)
    marks = models.IntegerField(choices=MARKS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    notes = models.CharField(max_length=500)

