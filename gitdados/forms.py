from django import forms

class GitDadosForm(forms.Form):
    git_name = forms.CharField(label="Git name", max_length=200)