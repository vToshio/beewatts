from .forms import EnderecoForm
from .models.endereco import Endereco
from .models.estado import Estado
from .models.cidade import Cidade
import requests

PVGIS_BASE_URL = 'https://re.jrc.ec.europa.eu/api/v5_2/PVcalc'
NOMINATIM_BASE_URL = 'https://nominatim.openstreetmap.org/search'

class GeolocalizacaoError(Exception):
    pass

class IrradianciaError(Exception):
    pass

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
        response.raise_for_status()
        
        data = response.json()
        return data['outputs']['totals']['fixed']['H(i)_m']
    except requests.RequestException as e:
        raise IrradianciaError(f'Erro ao Obter Irradiância: {str(e)}')

def obter_coordenadas(cidade: Cidade, logradouro: str) -> tuple[float, float] | None:
    '''
    Função auxiliar que busca pela geolocalização com base nos dados de endereço, utilizando a API Nominating 
    '''
    try:
        query = f'{logradouro}, {cidade.nome}, {cidade.estado.sigla}'
        response = requests.get(
            NOMINATIM_BASE_URL,
            params={
            'q': query,
            'format': 'json'
            },
            headers={
                'User-Agent': 'BeeWatts/1.0 (vtoshio@alunos.fho.edu.br)'
            }
        )
        response.raise_for_status()
        data = response.json()

        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        return (lat, lon)
    except requests.RequestException as e:
        raise GeolocalizacaoError(f'Erro ao Obter Geolocalização: {str(e)}')


def criar_endereco(cleaned: EnderecoForm) -> Endereco:
    '''
    Função auxiliar que define a lógica de registro de um novo endereço.
    '''
    try:
        uf, _ = Estado.objects.get_or_create(sigla=cleaned['uf'])
        cidade, _ = Cidade.objects.get_or_create(nome=cleaned['cidade'], estado=uf)
        logradouro = cleaned['logradouro']
        
        # Utilização do Nominating
        coordenadas = obter_coordenadas(cidade, logradouro)
        latitude = coordenadas[0]
        longitude = coordenadas[1]

        # Utilização da PVGIS
        irradiancia = obter_irradiancia(latitude, longitude)

        return Endereco.objects.create(
            cep = cleaned['cep'],
            cidade = cidade,
            logradouro = logradouro,
            irradiancia = irradiancia,
        )
    except (GeolocalizacaoError, IrradianciaError) as e:
        raise e