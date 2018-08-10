from django import forms
from django.forms import ModelForm
from .models import Question
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from django.urls import reverse

class InsQuestion(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ('branch', 'course', 'module', 'chapter', 'question', 'marks', 'priority')
        widgets = {
                #'question': forms.TextArea,
                'marks': forms.RadioSelect,
                'priority': forms.RadioSelect,
        }
        

    def __init__(self, *args, **kwargs):
        super(InsQuestion, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ins-question'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('index')
        self.helper.add_input(Submit('add', 'Add', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                Fieldset('Particular',
                          Field('branch', placeholder='Enter stream',
                                css_class="some-class"),
                          Field('course', placeholder='Enter Sub-Stream',
                                css_class="some-class"),
                          Field('module', placeholder='Enter Module name'),
                          Field('chapter', placeholder='Enter Chapter name'),),
                Fieldset('Question',
                            Field('question', placeholder='Enter your question here'),
                            InlineRadios('marks'),),
                Fieldset('Additional Information',
                            InlineRadios('priority'),))
