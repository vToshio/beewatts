from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Endereco, Concessionaria, PainelSolar, Simulacao
from .services import EnderecoService, SimulacaoService, GeolocalizacaoError, IrradianciaError
from .forms import EnderecoForm, DadosIniciaisForm
from uuid import UUID

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
                raise e
        else:
            messages.error(request, 'Erro ao registrar endereço, tente utilizar outro CEP')
    else:
        form = EnderecoForm()
    return render(request, 'simulador/endereco.html', {'form': form}) 

def dados_iniciais(request: HttpRequest):
    if request.method == 'POST':
        form = DadosIniciaisForm(request.POST)

        if form.is_valid():
            endereco = get_object_or_404(Endereco, cep=request.session.get('cep'))
            concessionaria = get_object_or_404(Concessionaria, id=form.cleaned_data['concessionaria_usuario'])
            painel = get_object_or_404(PainelSolar, id=form.cleaned_data['painel_usuario'])
            conta_luz = form.cleaned_data['conta_luz']
            area_disponivel = form.cleaned_data['area_disponivel']
            if area_disponivel is None:
                area_disponivel = 40

            simulacao, _ = Simulacao.objects.get_or_create(
                endereco=endereco,
                concessionaria=concessionaria,
                painel_solar=painel,
                conta_luz=conta_luz,
                area_disponivel=area_disponivel 
            )

            return redirect('visualizar_resultados', id=simulacao.id)
    else:
        form = DadosIniciaisForm()

    return render(request, 'simulador/dados_iniciais.html', {'form': form})

def resultados(request:HttpRequest, id:UUID):
    simulacao = get_object_or_404(Simulacao, id=id)
    service = SimulacaoService(simulacao=simulacao) 
    resultados = service.calcular_viabilidade(perdas=0.14)
    return render(request, 'simulador/resultado.html', {'simulacao': simulacao, 'dto': resultados})