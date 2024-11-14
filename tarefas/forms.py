from django import forms
from tarefas.models import Tarefas


class InsereUsuario(forms.ModelForm):
    class Meta:
    # Modelo base
        model = Usuario
    # Campos que estarão no form
        fields = [
            'nome',
            'email'
        ]
        # Campos que não estarão no form
        exclude = []

class InsereTarefa(forms.ModelForm):
    class Meta:
    # Modelo base
        model = Tarefas
    # Campos que estarão no form
        fields = [
            'descricao',
            'setor',
            'prioridade',
            'status',
            'data'
        ]
        # Campos que não estarão no form
        exclude = []