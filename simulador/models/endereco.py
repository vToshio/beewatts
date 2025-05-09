from django.db import models
from django.core.validators import RegexValidator

class Endereco(models.Model):
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
    uf = models.CharField(
        'Sigla (UF)',
        max_length=2,
        null=False,
        blank=False
    )
    cidade = models.CharField(
        'Cidade',
        max_length=50,
        null=False,
        blank=False
    )
    bairro = models.CharField(
        'Bairro',
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.cidade} ({self.cep})'