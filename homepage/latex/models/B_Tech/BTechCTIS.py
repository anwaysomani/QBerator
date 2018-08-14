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


# Enhancement of Communication Skills
class EOCS(models.Model):


# Engineering Design - I
class EDI(models.Model):



# Introduction to Computing Environment
class ITCE(models.Model):


# Bridge Course in Mathematics
class BCIM(models.Model):


# --B. Tech: Sem = 2--
# --------------------

# Differential Equations and Integral Calculus
class DEAIC(models.Model):


# Mechanics
class M(models.Model):


# Engineering Professionalism and Ethics
class EPAE(models.Model):


# Environmental Studies

# Computer Aided Engineering Graphics

# Engineering Design - II

# Bridge Course in Electronics


# --B. Tech: Sem - 3--
# --------------------

# Introdcution to Linux

# Software Engineering

# Computer Architecture and Organization

# Operating System Building Blocks

# Object Oriented Programming using Java

# Introduction to Communication Skills

# Data Structures and Algorithms


# --B. Tech: Sem - 4--
# --------------------

# Network Security Basics

# Introduction to Web Technology

# Database Management Systems

# Enterprise Network Engineering

# Cryptography Fundamentals

# Information Security

# Introduction to Public Speaking


# --B. Tech: Sem - 5--
# --------------------

# Fundamentals of Storage

# Principles of Virtualization

# Installation and Configuration of Server

# Reasoning and Thinking

# Ethical Hacking Fundamentals

# Free Elective - I

# Employability Skills


# --B. Tech: Sem - 6--
# --------------------

# Introduction to Cloud Technology

# Fundamentals of Data Center

# Linux Administration

# IT Governance, Risk and Information Security Management

# Database Security

# Free Elective - II

# Professional Skills



# --B. Tech: Sem - 7--
# --------------------

# Cloud Computing Solutions

# Cyber Forensics and Investigation

# Virtualization and Cloud Security

# Advanced Storage Technology

# Cloud Web Services

# Mini Project


# --B. Tech: Sem - 8--
# --------------------

# ITIL

# Entrepreneurship Development

# Major Project/Internship

