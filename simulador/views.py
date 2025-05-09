from django.shortcuts import render
from django.http import HttpRequest
from .forms import CepForm, EnderecoForm

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'simulador/index.html')

def endereco(request: HttpRequest):
    cep_form = CepForm()
    endereco_form = EnderecoForm()
    return render(request, 'simulador/endereco.html', {'cep_form': cep_form, 'endereco_form': endereco_form})