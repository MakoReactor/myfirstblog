from django import forms


class MeuCepForm(forms.Form):
    consulta_cep = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite um cep. Apenas Numeros.'}))
    


