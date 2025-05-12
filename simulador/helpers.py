from django.http import HttpResponseServerError
from .forms import EnderecoForm
from .models.endereco import Endereco
from .models.estado import Estado
from .models.cidade import Cidade
import requests

PVGIS_BASE_URL = 'https://re.jrc.ec.europa.eu/api/v5_2/PVcalc'

def obter_irradiancia(lat: float, lon: float) -> float:
    '''
    Função auxiliar que consulta a API da PVGIS para obter o índice de irradiância mensal (kWh/m³/mês).
    - Em caso de erro, retorna um HTTP 500
    '''
    try:
        response = requests.get(PVGIS_BASE_URL, params={
            'outputformat': 'json',
            'loss': 14,
            'peakpower': 1,
            'lat': lat,
            'lon': lon,
            'angle': round(abs(lat))
        })
        
        data = response.json()
        return data['outputs']['totals']['fixed']['H(i)_m']
    except Exception as e:
        raise HttpResponseServerError(str(e))

def criar_endereco(cleaned: EnderecoForm) -> Endereco:
    '''
    Função auxiliar que define a lógica de registro de um novo endereço.
    '''
    uf, _ = Estado.objects.get_or_create(sigla=cleaned['uf'])
    cidade, _ = Cidade.objects.get_or_create(nome=cleaned['cidade'], estado=uf)
    latitude = float(cleaned['latitude'])
    longitude = float(cleaned['longitude'])
    irradiancia = obter_irradiancia(latitude, longitude)
    
    return Endereco.objects.create(
        cep = cleaned.cleaned_data['cep'],
        cidade = cidade,
        logradouro = cleaned.cleaned_data['logradouro'],
        irradiancia = irradiancia,
    )