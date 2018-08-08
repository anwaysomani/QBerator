from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from django.urls import reverse

class InsQuestion(forms.Form):
    branch = forms.CharField(required=True, max_length=60)
    course = forms.CharField(required=True, max_length=60)
    module = forms.IntegerField(required=True)
    chapter = forms.IntegerField(required=True)
    question = forms.CharField(required=True, max_length=200, widget=forms.Textarea())
    marks = forms.TypedChoiceField(
        label="Select marks",
        choices=((0, "2"), (1, "5"), (2, "10")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        required=True)
    priority = forms.TypedChoiceField(
        label="Priority Level",
        choices=((0, "1"), (1, "2"), (2, "3"), (3, "4")),
        coerce=lambda y: bool(int(y)),
        widget=forms.RadioSelect,
        required=True)

    def __init__(self, *args, **kwargs):
        super(InsQuestion, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ins-question'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('index')
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
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
