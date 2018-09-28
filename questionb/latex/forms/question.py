from django import forms
from django.forms import ModelForm
from ..models import *

# Mock question form for trial pages
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = {'modules', 'question', 'marks', 'priority', 'notes'}
        widgets = { 
                   'marks': forms.RadioSelect,
                   'question': forms.Textarea(attrs={"placeholder": "Enter question here...", "rows": 5,"cols": 40,}),
                   'priority': forms.RadioSelect,
                   'modules': forms.Select(),
                   'notes': forms.Textarea(attrs={"placholder": "Special note...", "rows": 1, "cols": 25,}),
        }

