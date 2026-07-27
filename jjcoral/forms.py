from django import forms
from .models import Aluno, Turma, Treino, Exame, Inscricao, Presenca, Faixa, Professor, Coordenador


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('format', '%Y-%m-%d')
        super().__init__(*args, **kwargs)

class AlunoForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=DateInput()
    )

    data_inicio = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=DateInput()
    )
    class Meta:
        model = Aluno
        fields = ['nome', 'data_nascimento', 'faixa_atual', 'data_inicio', 'telefone', 'responsavel', 'foto']
        
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['usuario', 'nome', 'faixa', 'telefone', 'foto']

class CoordenadorForm(forms.ModelForm):
    class Meta:
        model = Coordenador
        fields = ['usuario', 'nome', 'faixa', 'telefone', 'foto']

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'horario', 'professor', 'alunos']
        widgets = {
            'alunos': forms.CheckboxSelectMultiple()
        }


class TreinoForm(forms.ModelForm):
    data = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=DateInput()
    ) # type: ignore
    class Meta:
        model = Treino
        fields = ['turma', 'data', 'conteudo']
    
        

class ExameForm(forms.ModelForm):
    data = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=DateInput()
    ) # type: ignore

    class Meta:
        model = Exame
        fields = ['aluno', 'data', 'faixa', 'resultado', 'avaliadores']


class FaixaForm(forms.ModelForm):
    class Meta:
        model = Faixa
        fields = ['nome', 'ordem', 'idade_minima', 'tempo_minimo_meses']

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ["status", "nota_tecnica", "nota_postura", "nota_disciplina", "comentarios"]

class PresencaForm(forms.ModelForm):
    class Meta:
        model = Presenca
        fields = ["presente"]
        