from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'data_inicio']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }