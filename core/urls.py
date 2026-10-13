from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:pk>/deletar/', views.deletar_projeto, name='deletar_projeto'),
]