from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario(nome=request.POST.get('nome'), idade=request.POST.get('idade'))
        novo_usuario.save()

    context = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', context)

def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.idade = request.POST.get('idade')
        usuario.save()
        return redirect('listagem_usuarios')
    return render(request, 'usuarios/editar.html', {'usuario': usuario})

def excluir_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listagem_usuarios')
    return render(request, 'usuarios/excluir.html', {'usuario': usuario})

def confirmar_excluir_todos(request):
    return render(request, 'usuarios/confirmar_exclusao_todos.html')

def excluir_todos(request):
    if request.method == 'POST':
        Usuario.objects.all().delete()  # Exclui todos os usuários
        return redirect('listagem_usuarios')  # Redireciona para a página de usuários
    return HttpResponse("Método não permitido", status=405)  # Retorna um erro se não for um POST
