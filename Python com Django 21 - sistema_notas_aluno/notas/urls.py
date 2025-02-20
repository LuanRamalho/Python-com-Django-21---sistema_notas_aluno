from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alunos, name='listar_alunos'),
    path('adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
    path('editar/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir/<int:aluno_id>/', views.excluir_aluno, name='excluir_aluno'),
]
