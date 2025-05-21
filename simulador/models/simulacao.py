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
    consumo_atual = models.IntegerField(
        'Consumo Médio Atual (kWh)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )
    quantidade_paineis = models.IntegerField(
        'Quantidade Necessária de Painéis',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )
    area_total = models.FloatField(
        'Área Total (m²)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )
    consumo_estimado = models.IntegerField(
        'Consumo Estimado (kWh)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False,
    )
    total_investimento = models.FloatField(
        'Total do Investimento (R$)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )
    tempo_payback = models.FloatField(
        'Tempo de Payback (Meses)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )
    custo_beneficio = models.FloatField(
        'Custo-benefício',
        null=False,
        blank=False
    )