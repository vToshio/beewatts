from django.shortcuts import render
from django.http import HttpRequest
from .forms import EnderecoForm

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'simulador/index.html')

def endereco(request: HttpRequest):
    form = EnderecoForm()
    return render(request, 'simulador/endereco.html', {'form': form})