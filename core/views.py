from django.shortcuts import render ##, redirect
from core.models import Evento
# Create your views here.

def lista_eventos(request):
    eventos = Evento.objects.all()
    dados = {'eventos': eventos}  ## Cria um dicionario com os eventos
    return render(request, 'agenda.html', dados)  ## Renderiza o template agenda.html

# def index(request):
#     return redirect('/agenda/')