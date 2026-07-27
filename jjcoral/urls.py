from django.urls import path
from . import views

app_name = "jjcoral"

urlpatterns = [

    
    # -------------------------
    # ALUNOS
    # -------------------------
    path('alunos/', views.AlunoListView.as_view(), name='aluno_lista'),
    path('alunos/novo/', views.AlunoCreateView.as_view(), name='aluno_novo'),
    path('alunos/<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detalhe'),
    path('alunos/<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='aluno_editar'),
    path('alunos/<int:pk>/deletar/', views.AlunoDeleteView.as_view(), name='aluno_deletar'),

    # -------------------------
    # COORDENADORES
    # -------------------------
    path('coordenadores/', views.CoordenadorListView.as_view(), name='coordenador_lista'),
    path('coordenadores/novo/', views.CoordenadorCreateView.as_view(), name='coordenador_novo'),
    path('coordenadores/<int:pk>/editar/', views.CoordenadorUpdateView.as_view(), name='coordenador_editar'),
    path('coordenadores/<int:pk>/deletar/', views.CoordenadorDeleteView.as_view(), name='coordenador_deletar'),

    # -------------------------
    # PROFESSORES
    # -------------------------
    path('professores/', views.ProfessorListView.as_view(), name='professor_lista'),
    path('professores/novo/', views.ProfessorCreateView.as_view(), name='professor_novo'),
    path('professores/<int:pk>/editar/', views.ProfessorUpdateView.as_view(), name='professor_editar'),
    path('professores/<int:pk>/deletar/', views.ProfessorDeleteView.as_view(), name='professor_deletar'),

    # -------------------------
    # TURMAS
    # -------------------------
    path('turmas/', views.TurmaListView.as_view(), name='turma_lista'),
    path('turmas/nova/', views.TurmaCreateView.as_view(), name='turma_nova'),
    path('turmas/<int:pk>/', views.TurmaDetailView.as_view(), name='turma_detalhe'),
    path('turmas/<int:pk>/editar/', views.TurmaUpdateView.as_view(), name='turma_editar'),
    path('turmas/<int:pk>/deletar/', views.TurmaDeleteView.as_view(), name='turma_deletar'),

    # -------------------------
    # TREINOS
    # -------------------------
    path('treinos/', views.TreinoListView.as_view(), name='treino_lista'),
    path('treinos/novo/', views.TreinoCreateView.as_view(), name='treino_novo'),
    path('treinos/<int:pk>/', views.TreinoDetailView.as_view(), name='treino_detalhe'),
    path('treinos/<int:pk>/presenca/', views.RegistrarPresencaView.as_view(), name='treino_presenca'),

    # -------------------------
    # Faixas
    # -------------------------
    path('faixas/', views.FaixaListView.as_view(), name='faixa_lista'),
    path('faixas/nova/', views.FaixaCreateView.as_view(), name='faixa_nova'),
    path('faixas/<int:pk>/', views.FaixaDetailView.as_view(), name='faixa_detalhe'),
    path('faixas/<int:pk>/editar/', views.FaixaUpdateView.as_view(), name='faixa_editar'),
    path('faixas/<int:pk>/deletar/', views.FaixaDeleteView.as_view(), name='faixa_deletar'),

    # -------------------------
    # EXAMES
    # -------------------------
    path('exames/', views.ExameListView.as_view(), name='exame_lista'),
    path('exames/novo/', views.ExameCreateView.as_view(), name='exame_novo'),
    path('exames/<int:pk>/', views.ExameDetailView.as_view(), name='exame_detalhe'),
    path('exames/<int:pk>/inscricoes/', views.InscricaoListView.as_view(), name='exame_inscricoes'),
    path('exames/<int:pk>/avaliar/<int:aluno_id>/', views.AvaliacaoView.as_view(), name='exame_avaliar'),

]
