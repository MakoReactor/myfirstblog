from django import forms

from .models import MeuCep


class MeuCepForm(forms.Form):
    consulta_cep = forms.CharField(widget.TextInput(attrs={'class':'form-control', 'placeholder':'Digite um cep. Apenas Numeros.'}))




class GitDadosForm(forms.Form):
    git_name = forms.CharField(label="Git name", max_length=200)
