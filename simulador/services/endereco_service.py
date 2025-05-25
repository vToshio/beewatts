from simulador.forms import EnderecoForm
from simulador.models.endereco import Endereco
from simulador.models.estado import Estado
from simulador.models.cidade import Cidade
from simulador.services.geolocalizacao_service import GeolocalizacaoService, GeolocalizacaoError
from simulador.services.irradiacao_service import IrradiacaoService, IrradianciaError

class EnderecoService:
    def criar_endereco(self, cleaned: EnderecoForm) -> Endereco:
        '''
        Função auxiliar que define a lógica de registro de um novo endereço.
        '''
        try:
            uf, _ = Estado.objects.get_or_create(sigla=cleaned['uf'])
            cidade, _ = Cidade.objects.get_or_create(nome=cleaned['cidade'], estado=uf)
            logradouro = cleaned['logradouro']
            
            # Utilização do Nominating
            geoloc_service = GeolocalizacaoService()
            coordenadas = geoloc_service.obter_coordenadas(cidade, logradouro)
            latitude = coordenadas[0]
            longitude = coordenadas[1]

            # Utilização da PVGIS
            irrad_service = IrradiacaoService()
            irradiancia = irrad_service.obter_irradiancia(latitude, longitude)

            return Endereco.objects.create(
                cep = cleaned['cep'],
                cidade = cidade,
                logradouro = logradouro,
                irradiancia = irradiancia,
            )
        except (GeolocalizacaoError, IrradianciaError) as e:
            raise e