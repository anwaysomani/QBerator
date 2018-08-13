from django import forms

class SemesterForm(forms.Form):
    SEM_CHOICES = [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
    ]
    semester = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

