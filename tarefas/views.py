from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefas
from .forms import TarefaForm

# Create your views here.

def listaTarefa(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')
    return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})

def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':tarefa})

def novaTarefa(request):

    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save()
            tarefa.save()
            return redirect('/')
    else:
        form = TarefaForm()
        return render(request, 'tarefas/addTarefa.html', {'form': form})
    
