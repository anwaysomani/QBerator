from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

class InsQuestion(forms.Form):
    branch = forms.CharField(required=True, max_length=60)
    course = forms.CharField(required=True, max_length=60)
    module = forms.IntegerField(required=True)
    chapter = forms.IntegerField(required=True)
    question = forms.CharField(required=True, max_length=200)
    marks = forms.IntegerField(required=True)
    priority = forms.IntegerField(required=True)
