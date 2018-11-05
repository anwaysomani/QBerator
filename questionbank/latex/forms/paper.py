from django import forms
from django.forms import ModelForm
from ..models import QuestionPaper

class PaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['Subject', 'QuestionPaper']
