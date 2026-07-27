from django.contrib.auth.models import User
from datetime import date
from django.db import models


# Cadastro do aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    data_nascimento = models.DateField()
    faixa_atual = models.ForeignKey("Faixa", on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField()
    telefone = models.CharField(max_length=20, blank=True)
    responsavel = models.CharField(max_length=120, blank=True)
    foto = models.ImageField(upload_to="alunos/", null=True, blank=True)

    @property
    def idade(self):
        hoje = date.today()
        return (
            hoje.year
            - self.data_nascimento.year
            - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))
        )
        
    def __str__(self):
        return self.nome

# Faixa de graduação do aluno
class Faixa(models.Model):
    nome = models.CharField(max_length=20)
    ordem = models.IntegerField()  # branca=1, cinza=2, etc.
    idade_minima = models.IntegerField()
    tempo_minimo_meses = models.IntegerField()

    def __str__(self):
        return self.nome

# Cadastro do professor
class Professor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    faixa = models.ForeignKey(Faixa, on_delete=models.SET_NULL, null=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='professores/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Coordenador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    faixa = models.ForeignKey(Faixa, on_delete=models.SET_NULL, null=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='coordenadores/', blank=True, null=True)

    def __str__(self):
        return self.nome


# Turma de alunos, com horário e professor responsável
class Turma(models.Model):
    nome = models.CharField(max_length=50)
    horario = models.TimeField()
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    alunos = models.ManyToManyField(Aluno, related_name="turmas")

    def __str__(self):
        return self.nome

# Treino realizado em uma determinada turma, com data e conteúdo
class Treino(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data = models.DateField()
    conteudo = models.TextField()
    instrutor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.turma} - {self.data}"

# Presença do aluno em um treino específico
class Presenca(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    presente = models.BooleanField(default=True)

# Exame de graduação, com data, faixa e avaliadores
class Exame(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField()
    faixa = models.ForeignKey(Faixa, on_delete=models.CASCADE)
    avaliadores = models.ManyToManyField(Professor, related_name="avaliacoes")
    resultado = models.TextField(blank=True)

    def __str__(self):
        return f"Exame {self.faixa.nome} - {self.data}"

# Inscrição do aluno em um exame, com status e notas
class Inscricao(models.Model):
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),
        ("reprovado", "Reprovado"),
    ])
    nota_tecnica = models.IntegerField(null=True, blank=True)
    nota_postura = models.IntegerField(null=True, blank=True)
    nota_disciplina = models.IntegerField(null=True, blank=True)
    comentarios = models.TextField(blank=True)
