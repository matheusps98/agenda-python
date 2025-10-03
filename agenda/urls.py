"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),  ## Inclui as urls do app core
    # path('', views.index),  ## Rota raiz para a view index
    path('agenda/evento', views.evento),  ## Rota para a view evento
    # Rota para EDITAR um evento existente (passando o ID na URL)
    path('agenda/evento/<int:id_evento>/', views.evento, name='evento_editar'),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),  ## Rota para deletar evento, passando o id do evento como parametro
    path('agenda/evento/submit/', views.submit_evento),  ## Rota para submissão do formulário de evento
    path('',RedirectView.as_view(url='/agenda/')),  ## Redireciona a rota raiz para /agenda/
    path('login/', views.login_user),  ## Rota para a view de login
    path('login/submit', views.submit_login),  ## Rota para a view de login
    path('logout/', views.logout_user),  ## Rota para a view de logout
]
    