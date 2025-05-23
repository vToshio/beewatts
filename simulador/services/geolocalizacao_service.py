from simulador.models.cidade import Cidade
import requests

class GeolocalizacaoError(Exception):
    pass

class GeolocalizacaoService:
    _NOMINATIM_URL:str = 'https://nominatim.openstreetmap.org/search'

    @classmethod
    def obter_coordenadas(cls, cidade: Cidade, logradouro: str) -> tuple[float, float] | None:
        '''
        Função auxiliar que busca pela geolocalização com base nos dados de endereço, utilizando a API Nominating 
        '''
        try:
            query = f'{logradouro}, {cidade.nome}, {cidade.estado.sigla}'
            response = requests.get(
                cls._NOMINATIM_URL,
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