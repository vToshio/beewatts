# 🐝🌞 BeeWatts - Calculadora de Viabilidade Solar

Este projeto é uma aplicação web desenvolvida em Django para simulação de viabilidade de sistemas de energia solar fotovoltaica. O sistema permite ao usuário inserir dados sobre consumo de energia, localização, área disponível e características dos painéis solares, retornando informações como economia estimada, quantidade de painéis necessários, investimento, payback e uso prático da energia gerada.

## Tecnologias Utilizadas
- Python 3.13
- Django 5.2
- Gunicorn
- Whitenoise
- PostgreSQL
- HTML, CSS, JavaScript

## Instalação e Execução Local
1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd projeto-deploy
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
6. Acesse em [http://localhost:8000](http://localhost:8000)

## Deploy (Railway)
- O projeto está preparado para deploy no Railway, utilizando Gunicorn e Whitenoise.
- Arquivos importantes para deploy:
  - `Procfile`
  - `runtime.txt`
  - `requirements.txt`
- Recomenda-se configurar as variáveis de ambiente para banco de dados e Django Secret Key.

## Estrutura do Projeto
- `manage.py`: utilitário de gerenciamento do Django
- `setup/`: configurações do projeto
- `simulador/`: app principal com lógica de simulação
- `navegacao/`: app para navegação e páginas estáticas
- `static/` e `templates/`: arquivos estáticos e templates HTML

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
