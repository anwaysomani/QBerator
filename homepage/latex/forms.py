from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from django.urls import reverse

class InsQuestion(forms.Form):
    branch = forms.CharField(required=True, max_length=60)
    course = forms.CharField(required=True, max_length=60)
    module = forms.IntegerField(required=True)
    chapter = forms.IntegerField(required=True)
    question = forms.CharField(required=True, max_length=200)
    marks = forms.IntegerField(required=True)
    priority = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(InsQuestion, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ins-question'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('index')
        self.helper.add_input(Submit('submit', 'Submit'))   
