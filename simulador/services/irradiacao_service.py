import requests

class IrradianciaError(Exception):
    pass

class IrradiacaoService:
    _PVGIS_URL:str = 'https://re.jrc.ec.europa.eu/api/v5_2/PVcalc'

    @classmethod
    def obter_irradiancia(cls, lat: float, lon: float) -> float:
        '''
        Função auxiliar que consulta a API da PVGIS para obter o índice de irradiância mensal (kWh/m³/mês).
        - Em caso de erro, retorna um HTTP 500
        '''
        try:
            response = requests.get(cls._PVGIS_URL, params={
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