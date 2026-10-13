from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto
from .forms import ProjetoForm

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/listar_projetos.html', {'projetos': projetos})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'core/form_projeto.html', {'form': form, 'titulo': 'Novo Projeto'})


def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'frequencia/form_projeto.html', {'form': form, 'titulo': 'Editar Projeto'})

def deletar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('listar_projetos')
    return render(request, 'frequencia/confirmar_delecao.html', {'projeto': projeto})