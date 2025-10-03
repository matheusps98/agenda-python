from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento') ## verbose_name altera o nome do campo na interface de admin
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  ## CASCADE deleta todos os eventos do usuario se o usuario for deletado
    local = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'evento'


    def __str__(self):
        return self.titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y')
    
    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y')
    def get_hora_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')