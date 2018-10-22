from django import forms
from django.forms import ModelForm
from ..models import *

# Mock question form for trial pages
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = {'block', 'modules', 'question', 'marks', 'priority', 'notes'}
        widgets = { 
                   'modules': forms.Select(),
                   'question': forms.Textarea(attrs={"placeholder": "Enter question here...", "rows": 5,"cols": 40,}),
                   'marks': forms.Select(),
                   'priority': forms.Select(),
                   'notes': forms.Textarea(attrs={"placholder": "Special note...", "rows": 1, "cols": 25,}),
        }

