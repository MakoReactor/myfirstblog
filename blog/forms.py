from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite um título para a postagem'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Digite um texto','rows':25 }))
    #text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Post
        fields = ('title', 'text')
