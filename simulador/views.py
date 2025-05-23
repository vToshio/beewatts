from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Endereco, Concessionaria, PainelSolar
from .services import EnderecoService, GeolocalizacaoError, IrradianciaError
from .forms import EnderecoForm, DadosIniciaisForm

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
                service = EnderecoService()
                endereco = service.criar_endereco(cleaned=form.cleaned_data)
                request.session['cep'] = endereco.cep
                return redirect('registrar_dados')
            except (GeolocalizacaoError, IrradianciaError):
                messages.error(request, 'Erro de geolocalização ao registrar endereço, tente utilizar outro CEP')
            except Exception as e:
                print(e)
                messages.error(request, 'Erro interno do servidor')
        else:
            messages.error(request, 'Erro ao registrar endereço, tente utilizar outro CEP')
    else:
        form = EnderecoForm()
    return render(request, 'simulador/endereco.html', {'form': form}) 

def dados_iniciais(request: HttpRequest):
    form = DadosIniciaisForm()
    return render(request, 'simulador/dados_iniciais.html', {'form': form})

def calcular_viabilidade(request: HttpRequest):
    if request.method == 'POST':
        form = DadosIniciaisForm(request.POST)
        if form.is_valid():
            endereco: Endereco = Endereco.objects.filter(cep=request.session['cep']).first()
            consumo_usuario: int = form.cleaned_data['consumo_usuario']
            area_disponivel: float = form.cleaned_data['area_disponivel']
            concessionaria: Concessionaria = get_object_or_404(Concessionaria, id=form.cleaned_data['concessionaria_usuario'])
            painel_solar: PainelSolar = get_object_or_404(PainelSolar, id=form.cleaned_data['painel_usuario'])

            print(endereco, consumo_usuario, area_disponivel, concessionaria, painel_solar, sep=' - ')
    return redirect('registrar_dados')