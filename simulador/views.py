from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models.endereco import Endereco
from .helpers import criar_endereco
from .forms import EnderecoForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'simulador/index.html')

@csrf_exempt
def endereco(request: HttpRequest):
    request.session['ultima_url'] = request.path
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            cep: str = form.cleaned_data['cep']
            if Endereco.objects.filter(cep=cep).exists():
                request.session['cep'] = cep
                return redirect('registrar_dados')
            
            endereco = criar_endereco(form.cleaned_data)
            endereco.save()
            request.session['cep'] = endereco.cep
            return redirect('registrar_dados')
    else:
        form = EnderecoForm()
    return render(request, 'simulador/endereco.html', {'form': form}) 

def dados_iniciais(request: HttpRequest):
    return render(request, 'simulador/dados_iniciais.html', {'cep': request.session.get('cep', None)})