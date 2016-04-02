from django import forms

__author__ = 'benjamin.c.yan'


class NameForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
