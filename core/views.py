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