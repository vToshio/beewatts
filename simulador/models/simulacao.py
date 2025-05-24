from django.db import models
from simulador.validators import validar_positivo
from .endereco import Endereco
from .painel_solar import PainelSolar
from .concessionaria import Concessionaria
from uuid import uuid4

class Simulacao(models.Model):
    class Meta:
        db_table = 'simulacoes'

    id = models.UUIDField(
        unique=True,
        default=uuid4, 
        primary_key=True
    )
    endereco = models.ForeignKey(
        to=Endereco,
        on_delete=models.PROTECT
    )
    painel_solar = models.ForeignKey(
        to=PainelSolar,
        on_delete=models.PROTECT
    )
    concessionaria = models.ForeignKey(
        to=Concessionaria,
        on_delete=models.PROTECT
    )
    conta_luz = models.FloatField(
        'Valor da Conta de Luz (R$)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False,
        default=0
    )
    area_disponivel = models.FloatField(
        'Área para Instalação (m²)',
        validators=[
            validar_positivo,
        ],
        null=True,
        blank=True,
        default=40.0
    )