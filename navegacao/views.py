from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'navegacao/index.html')

def sobre(request: HttpRequest):
    return render(request, 'navegacao/sobre.html')

def teste(request: HttpRequest):
    return render(request, 'navegacao/teste.html')

def termo_privacidade(request: HttpRequest):
    return render(request, 'navegacao/termo_privacidade.html')

def requisicao_invalida(request: HttpRequest, exception):
    return render(request, 'navegacao/400_template.html')

def acesso_proibido(request: HttpRequest, exception):
    return render(request, 'navegacao/403_template.html')

def pagina_nao_encontrada(request: HttpRequest, exception):
    return render(request, 'navegacao/404_template.html')

def erro_interno(request: HttpRequest):
    return render(request, 'navegacao/500_template.html')