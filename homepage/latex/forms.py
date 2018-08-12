from django import forms
from django.db import models
from .models import Branch, Specialization, Semester, Course, Module, Chapter, Question, Marks, Additional

class InsertQuestion(forms.ModelForm):
     branch = forms.ModelChoiceField(queryset=models.Branch.objects.all())
     specialization = forms.ModelChoiceField(queryset=models.Specialization.objects.none())
     chapter = forms.ModelChoiceField(queryset=models.Chapter.objects.none())
     course = forms.ModelChoiceField(queryset=models.Course.objects.none())
     module= forms.ModelChoiceField(queryset=models.Module.objects.none())
     chapter = forms.ModelChoiceField(queryset=models.Chapter.objects.none())
     question= forms.ModelChoiceField(queryset=models.Question.objects.none())
     marks = forms.ModelChoiceField(queryset=models.Marks.objects.all())
     priority = forms.ModelChoiceField(queryset=models.Additonal.objects.all())
     note = forms.ModelChoiceField(queryset=models.Additonal.objects.none())

     class Meta:
            model = models.Chapter, models.Question, models.Marks, models.Additional

            fields = ('branch', 'specialization', 'semester', 'course', 'module', 'chapter', 'question', 'marks', 'priority', 'note')
