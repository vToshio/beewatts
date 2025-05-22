from django.db import models
from django.core.validators import RegexValidator
from .cidade import Cidade

class Endereco(models.Model):
    class Meta:
        db_table = 'enderecos'

    id = models.AutoField(primary_key=True)
    cep = models.CharField(
        'CEP',
        validators=[
            RegexValidator(
                regex=r'[\d]{8}',
                message='Insira apenas os 8 dígitos do CEP'
            )
        ],
        max_length=8,
        unique=True,
        null=False,
        blank=False
    )
    cidade = models.ForeignKey(
        to=Cidade,
        on_delete=models.CASCADE
    )
    logradouro = models.CharField(
        'Logradouro',
        max_length=100,
        null=True,
        blank=True
    )
    irradiancia = models.FloatField(
        'Índice de Irradiância (kWh/m²/mês)',
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.cep} - {self.cidade}'