# Agenda Python

Este é um projeto prático de agenda de compromissos desenvolvido em Django.

## Funcionalidades
- Cadastro de usuários e autenticação (login/logout)
- Listagem de agendamentos do usuário logado
- Criação, edição e exclusão de agendamentos
- Campo de local do evento
- Indicação visual de eventos vencidos ("(vencida)" no título)
- Interface responsiva e moderna com destaque para botões e navbar
- Mensagens de sucesso e erro para ações do usuário

## Tecnologias Utilizadas
- Python 3.13+
- Django 5.2+
- SQLite (banco de dados padrão)
- HTML5, CSS3, JavaScript
- Bootstrap e FontAwesome (opcional para ícones)

## Como rodar o projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/matheusps98/agenda-python.git
   cd agenda-python
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Realize as migrações do banco:
   ```bash
   python manage.py migrate
   ```
5. Crie um superusuário (opcional, para acessar o admin):
   ```bash
   python manage.py createsuperuser
   ```
6. Rode o servidor:
   ```bash
   python manage.py runserver
   ```
7. Acesse em [http://127.0.0.1:8000/agenda/](http://127.0.0.1:8000/agenda/)

## Estrutura de Pastas
- `agenda/` - Configurações do projeto Django
- `core/` - App principal com models, views, templates
- `templates/` - HTMLs do sistema
- `static/` - (opcional) arquivos estáticos (CSS, JS, imagens)

## Observações
- O projeto marca automaticamente eventos vencidos na listagem.
- O campo "local" é obrigatório para novos eventos.
- O design pode ser customizado em `templates/models/navbar.html` e nos arquivos de template.

## Licença
MIT
