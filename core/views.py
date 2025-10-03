from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento(request, id_evento=None):
    if id_evento:
        evento = Evento.objects.get(id=id_evento)
        dados = {'evento': evento}
        return render(request, 'evento.html', dados)
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos}  ## Cria um dicionario com os eventos
    return render(request, 'agenda.html', dados)  ## Renderiza o template agenda.html

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/agenda/')
        else:
            messages.error(request, "Usuário ou senha inválido.")
            return redirect('/login/')
    else:
        return redirect('/')
    
@login_required(login_url='/login/')    
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if evento.usuario == usuario:
        evento.delete()
        messages.success(request, "Evento deletado com sucesso.")
    else:
        messages.error(request, "Você não tem permissão para deletar este evento.")
    return redirect('/agenda/')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        local = request.POST.get('local')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Evento.objects.filter(id=id_evento).update(titulo=titulo, descricao=descricao, data_evento=data_evento, local=local)
        else:
             Evento.objects.create(titulo=titulo, descricao=descricao, data_evento=data_evento, usuario=usuario, local=local)
        
    return redirect('/')
# def index(request):
#     return redirect('/agenda/')