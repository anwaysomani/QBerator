from django import forms
from .models import CreateQuestion

class CreateQuestion(forms.ModelForm):
    class Meta:
        model = CreateQuestion
        fields = ['branch', 'specialization', 'semester', 'course', 'module', 'chapter', 'question', 'marks', 'priority', 'notes']

    def clean(self):
        cleaned_data = super(CreateQuestion, self).clean()
        branch = cleaned_data.get('branch')
        specialization = cleaned_data.get('specialization')
        semester = cleaned_data.get('semester')
        course = cleaned_data.get('course')
        module = cleaned_data.get('module')
        chapter = cleaned_data.get('chapter')
        question = cleaned_data.get('question')
        marks = cleaned_data.get('marks')
        priority = cleaned_data.get('priority')
        notes = cleaned_data.get('notes')

        if not branch and not specialization and not semester and not course and not module and not chapter and not question and not marks:
            raise forms.ValidationError('Fill in all the fields!')
