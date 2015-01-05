# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    files = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    jjal_text = forms.CharField(max_length=200)