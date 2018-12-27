"""
Form for creating question
Inside app: latex

Developer: Anway Somani

"""

from django import forms
from django.forms import ModelForm
from ..models import Question

# Mock question form for trial pages
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = {'block', 'modules', 'question', 'marks', 'priority', 'notes'}
        widgets = {
                   'block': forms.TextInput(attrs={'readonly': True}),
                   'modules': forms.Select(),
                   'question': forms.Textarea(attrs={"placeholder": "Enter any question here...", "rows": 5,"cols": 100,}),
                   'marks': forms.Select(),
                   'priority': forms.Select(),
                   'notes': forms.Textarea(attrs={"placholder": "Special note...", "rows": 5, "cols": 100,}),
        }

        def save(self):
            if not self.id:
                self.block = subject.id()
            super(QuestionForm, self).save()
