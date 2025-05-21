from django.db import models
from simulador.validators import validar_positivo

class PainelSolar(models.Model):
    class Meta:
        db_table = 'paineis_solares'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        'Nome do Painel',
        unique=True,
        max_length=50,
        null=True,
        blank=True,
    )
    valor = models.FloatField(
        'Valor (R$)', 
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )   
    potencia = models.IntegerField(
        'Potência (W)',
        validators=[
            validar_positivo,
        ],
        null=False,
        blank=False
    )
    altura = models.FloatField(
        'Altura (m)',
        validators=[
            validar_positivo,
        ],
        null = False,
        blank=False
    )
    largura = models.FloatField(
        'Largura (m)',
        validators=[
            validar_positivo,
        ],
        null = False,
        blank=False
    )
    area = models.DecimalField(
        'Área (m²)',
        null=False,
        blank=False,
        max_digits=2,
        decimal_places=2
    )

    def save(self, *args, **kwargs):
        self.nome = f'{self.potencia} W'
        self.area = self.largura * self.altura
        return super().save(*args, **kwargs)