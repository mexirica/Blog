from django import forms

class ContatoForms(forms.Form):
    nome = forms.CharField(max_length=100, required=True, label="Nome")
    email= forms.EmailField(required=True, label="Email")
    telefone= forms.IntegerField(required=True, label="Telefone")
    mensagem= forms.CharField(widget=forms.Textarea, label="Mensagem")