from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from .models import Usuario
from .forms import UsuarioForm
# Create your views here.


def index(request):
    return render(request, 'usuario/index.html')


def create_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Cadastro Efetuado com Sucesso!!!'
            )
            return redirect('usuario')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/cadastro.html', {'form': form})
