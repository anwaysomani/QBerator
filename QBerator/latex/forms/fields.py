from django import forms
from django.forms import ModelForm
from ..models import *

class Branch(forms.ModelForm):
    class Meta: 
        fields = ['branch', 'br_abbr']
        labels = {
            'branch': 'Branch',
            'br_abbr': 'Abbreviation',
        }

class Specialization(forms.ModelForm):
    class Meta:
        labels = {
            'specialization1': 'First Specialization',
            'specialization2': 'Second Specilization(if any)',
        }

