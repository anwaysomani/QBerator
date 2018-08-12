from django import forms
from django.db import models
from .models import Branch, Specialization, Semester, Course, Module, Chapter, Question, Marks, Additional

class InsertQuestion(forms.ModelForm):
     branch = forms.ModelChoiceField(queryset=Branch.objects.all())
     specialization = forms.ModelChoiceField(queryset=Specialization.objects.none())
     chapter = forms.ModelChoiceField(queryset=.Chapter.objects.none())
     course = forms.ModelChoiceField(queryset=Course.objects.none())
     module= forms.ModelChoiceField(queryset=Module.objects.none())
     chapter = forms.ModelChoiceField(queryset=Chapter.objects.none())
     question= forms.ModelChoiceField(queryset=Question.objects.none())
     marks = forms.ModelChoiceField(queryset=Marks.objects.all())
     priority = forms.ModelChoiceField(queryset=Additonal.objects.all())
     note = forms.ModelChoiceField(queryset=Additonal.objects.none())

     class Meta:
            model = models.Chapter, models.Question, models.Marks, models.Additional

            fields = ('branch', 'specialization', 'semester', 'course', 'module', 'chapter', 'question', 'marks', 'priority', 'note')
