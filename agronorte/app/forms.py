from django import forms

class ClienteForm(forms.Form):
    nome = forms.CharField(label="Nome do cliente: ", max_length=100)
    idade = forms.IntegerField(label="Idade: ")
    data_nascimento = forms.DateField(label="Data de nascimento: ")
    is_ativo = forms.BooleanField(label="Está ativo: ")
    