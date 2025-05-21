from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'navegacao/index.html')

def sobre(request: HttpRequest):
    return render(request, 'navegacao/sobre.html')

def teste(request: HttpRequest):
    return render(request, 'navegacao/teste.html', {'teste': 'variável gay'})