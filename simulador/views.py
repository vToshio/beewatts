from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models.endereco import Endereco
from .helpers import criar_endereco, IrradianciaError, GeolocalizacaoError
from .forms import EnderecoForm

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'simulador/index.html')

def endereco(request: HttpRequest):
    request.session['ultima_url'] = request.path
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            cep: str = form.cleaned_data['cep']
            if Endereco.objects.filter(cep=cep).exists():
                request.session['cep'] = cep
                return redirect('registrar_dados')
            
            try:
                endereco = criar_endereco(form.cleaned_data)
                request.session['cep'] = endereco.cep
                return redirect('registrar_dados')
            except (GeolocalizacaoError, IrradianciaError):
                messages.error(request, 'Erro de geolocalização ao registrar endereço, tente utilizar outro CEP')
            except Exception:
                messages.error(request, 'Erro interno do servidor')
        else:
            messages.error(request, 'Erro ao registrar endereço, tente utilizar outro CEP')
    else:
        form = EnderecoForm()
    return render(request, 'simulador/endereco.html', {'form': form}) 

def dados_iniciais(request: HttpRequest):
    return render(request, 'simulador/dados_iniciais.html', {'cep': request.session.get('cep', None)})