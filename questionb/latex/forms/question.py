from django import forms
from django.forms import ModelForm
from .models import *



# Mock question form for trial pages
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = {'modules', 'question', 'marks', 'priority', 'notes'}
        widgets = { 
                   'marks': forms.RadioSelect,
                   'priority': forms.RadioSelect,
        }


