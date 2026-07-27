from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    AlunoForm, TurmaForm, TreinoForm, FaixaForm, CoordenadorForm,
    ExameForm, AvaliacaoForm, PresencaForm, ProfessorForm
)
from .models import Aluno, Turma, Treino, Exame, Inscricao, Presenca, Faixa, Professor, Coordenador
from django.views.generic import (
    FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .mixins import ProfessorRequiredMixin
from django.contrib.auth.models import Group


# Home view
def home(request):
    return render(request, "home.html")

# View para atualizar informações do aluno
class AlunoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "jjcoral/alunos/aluno_form.html"
    success_url = reverse_lazy("jjcoral:aluno_lista")
    success_message = "Aluno cadastrado com sucesso."

class AlunoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "jjcoral/alunos/aluno_form.html"
    success_url = reverse_lazy("jjcoral:aluno_lista")
    success_message = "Aluno atualizado com sucesso."

class AlunoListView(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = "jjcoral/alunos/aluno_lista.html"
    context_object_name = "alunos"
    

class AlunoDetailView(LoginRequiredMixin, DetailView):
    model = Aluno
    template_name = "jjcoral/alunos/aluno_detalhe.html"
    context_object_name = "aluno"


class AlunoDeleteView(LoginRequiredMixin, DeleteView):
    model = Aluno
    template_name = "jjcoral/alunos/aluno_confirm_delete.html"
    success_url = reverse_lazy("jjcoral:aluno_lista")
# ===============================

# Views para Professores
class ProfessorCreateView(LoginRequiredMixin, CreateView):
    model = Professor
    form_class = ProfessorForm
    template_name = "jjcoral/professores/professor_form.html"
    success_url = reverse_lazy("jjcoral:professor_lista")
    
    def form_valid(self, form):
        response = super().form_valid(form) # type: ignore
        grupo = Group.objects.get(name="Professor")
        self.object.usuario.groups.add(grupo) # type: ignore
        return response

class ProfessorListView(LoginRequiredMixin, ListView):
    model = Professor
    template_name = "jjcoral/professores/professor_lista.html"
    context_object_name = "professores"

class ProfessorUpdateView(LoginRequiredMixin, UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = "jjcoral/professores/professor_form.html"
    success_url = reverse_lazy("jjcoral:professor_lista")


class ProfessorDeleteView(LoginRequiredMixin, DeleteView):
    model = Professor
    template_name = "jjcoral/professores/professor_confirm_delete.html"
    success_url = reverse_lazy("jjcoral:professor_lista")
# ==============================

# Views para Coordenadores
class CoordenadorListView(LoginRequiredMixin, ListView):
    model = Coordenador
    template_name = "jjcoral/coordenadores/coordenador_lista.html"
    context_object_name = "coordenadores"


class CoordenadorCreateView(LoginRequiredMixin, CreateView):
    model = Coordenador
    form_class = CoordenadorForm
    template_name = "jjcoral/coordenadores/coordenador_form.html"
    success_url = reverse_lazy("jjcoral:coordenador_lista")

    def form_valid(self, form):
        response = super().form_valid(form)
        grupo = Group.objects.get(name="Coordenador")
        self.object.usuario.groups.add(grupo)
        return response


class CoordenadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Coordenador
    form_class = CoordenadorForm
    template_name = "jjcoral/coordenadores/coordenador_form.html"
    success_url = reverse_lazy("jjcoral:coordenador_lista")


class CoordenadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Coordenador
    template_name = "jjcoral/coordenadores/coordenador_confirm_delete.html"
    success_url = reverse_lazy("jjcoral:coordenador_lista")

# Views para Turmas
class TurmaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = "jjcoral/turmas/turma_form.html"
    success_url = reverse_lazy("jjcoral:turma_lista")
    success_message = "Turma criada com sucesso."

class TurmaListView(LoginRequiredMixin, ListView):
    model = Turma
    template_name = "jjcoral/turmas/turma_lista.html"
    context_object_name = "turmas"

class TurmaDetailView(LoginRequiredMixin, DetailView):
    model = Turma
    template_name = "jjcoral/turmas/turma_detalhe.html"
    context_object_name = "turma"

class TurmaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = "jjcoral/turmas/turma_form.html"
    success_url = reverse_lazy("jjcoral:turma_lista")
    success_message = "Turma atualizada com sucesso."


class TurmaDeleteView(LoginRequiredMixin, DeleteView):
    model = Turma
    template_name = "jjcoral/turmas/turma_confirm_delete.html"
    success_url = reverse_lazy("jjcoral:turma_lista")
# ===============================

# Views para Treinos
class TreinoCreateView(LoginRequiredMixin, ProfessorRequiredMixin, SuccessMessageMixin, CreateView):
    model = Treino
    form_class = TreinoForm
    template_name = "jjcoral/treinos/treino_form.html"
    success_url = reverse_lazy("jjcoral:treino_lista")
    success_message = "Treino registrado com sucesso."

class TreinoListView(LoginRequiredMixin, ListView):
    model = Treino
    template_name = "jjcoral/treinos/treino_lista.html"
    context_object_name = "treinos"


class TreinoDetailView(LoginRequiredMixin, DetailView):
    model = Treino
    template_name = "jjcoral/treinos/treino_detalhe.html"
    context_object_name = "treino"
# ===============================

# Views das faixas de graduação
class FaixaListView(LoginRequiredMixin, ListView):
    model = Faixa
    template_name = "jjcoral/faixas/faixa_lista.html"
    context_object_name = "faixas"


class FaixaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Faixa
    form_class = FaixaForm
    template_name = "jjcoral/faixas/faixa_form.html"
    success_url = reverse_lazy("jjcoral:faixa_lista")
    success_message = "Faixa cadastrada com sucesso."


class FaixaDetailView(LoginRequiredMixin, DetailView):
    model = Faixa
    template_name = "jjcoral/faixas/faixa_detalhe.html"
    context_object_name = "faixa"


class FaixaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Faixa
    form_class = FaixaForm
    template_name = "jjcoral/faixas/faixa_form.html"
    success_url = reverse_lazy("jjcoral:faixa_lista")
    success_message = "Faixa atualizada com sucesso."


class FaixaDeleteView(LoginRequiredMixin, DeleteView):
    model = Faixa
    template_name = "jjcoral/faixas/faixa_confirm_delete.html"
    success_url = reverse_lazy("jjcoral:faixa_lista")

# Views para Exames e Inscrições

class ExameCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Exame
    form_class = ExameForm
    template_name = "jjcoral/exames/exame_form.html"
    success_url = reverse_lazy("jjcoral:exame_lista")
    success_message = "Exame criado com sucesso."

class ExameListView(LoginRequiredMixin, ListView):
    model = Exame
    template_name = "jjcoral/exames/exame_lista.html"
    context_object_name = "exames"

class ExameDetailView(LoginRequiredMixin, DetailView):
    model = Exame
    template_name = "jjcoral/exames/exame_detalhe.html"
    context_object_name = "exame"

class InscricaoListView(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = "jjcoral/exames/inscricoes.html"
    context_object_name = "inscricoes"

    def get_queryset(self):
        exame_id = self.kwargs["pk"]
        return Inscricao.objects.filter(exame_id=exame_id).select_related("aluno", "exame")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exame_id = self.kwargs["pk"]
        context["exame"] = get_object_or_404(Exame, pk=exame_id)
        return context

# ===============================

# Registrar presença dos alunos em um treino específico
class RegistrarPresencaView(LoginRequiredMixin, ProfessorRequiredMixin, FormView):
    template_name = "jjcoral/treinos/presenca.html"

    def get_form(self): # type: ignore
        treino = Treino.objects.get(pk=self.kwargs["pk"])
        alunos = Aluno.objects.all()

        class PresencaForm(forms.Form):
            presentes = forms.ModelMultipleChoiceField(
                queryset=alunos,
                widget=forms.CheckboxSelectMultiple,
                required=False
            )

        return PresencaForm(**self.get_form_kwargs())

    def form_valid(self, form):
        treino = Treino.objects.get(pk=self.kwargs["pk"])
        presentes = form.cleaned_data["presentes"]

        Presenca.objects.filter(treino=treino).delete()

        for aluno in presentes:
            Presenca.objects.create(treino=treino, aluno=aluno, presente=True)

        return redirect("jjcoral:treino_detalhe", pk=treino.pk)
# ===============================

# Views para Avaliação de Exames
class AvaliacaoView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Inscricao
    form_class = AvaliacaoForm
    template_name = "jjcoral/exames/avaliacao.html"

    def get_object(self): # type: ignore
        exame_id = self.kwargs["pk"]
        aluno_id = self.kwargs["aluno_id"]
        return get_object_or_404(Inscricao, exame_id=exame_id, aluno_id=aluno_id)

    def get_success_url(self):
        return reverse_lazy("jjcoral:exame_inscricoes", kwargs={"pk": self.kwargs["pk"]})
